local http = require "resty.http"
local cjson = require("cjson")

local AuthenticationHandler = {
    VERSION = "1.0",
    PRIORITY = 1000,
}

local function verify_access_token(conf, access_token)
    local httpc = http:new()
    local headers = {
        ["Authorization"] = "Bearer " .. access_token,
    }

    local res, err = httpc:request_uri(conf.authentication_verify_endpoint, {
        method = "GET",
        ssl_verify = false,
        headers = headers,
    })

    if not res then
        kong.log.err("failed to reach authentication endpoint: ", err)
        return kong.response.exit(500)
    end
    
    if res.status ~= 200 then
        kong.log.err("failed to verify access token: ", res.status)
        return kong.response.exit(401)
    end

    return true
end

local function get_access_token_info(conf, access_token)
    local httpc = http:new()
    local headers = {
        ["Authorization"] = "Bearer " .. access_token,
    }

    local res, err = httpc:request_uri(conf.authentication_info_endpoint, {
        method = "GET",
        ssl_verify = false,
        headers = headers,
    })

    if not res then
        kong.log.err("failed to reach authentication endpoint: ", err)
        return kong.response.exit(500)
    end
    
    if res.status ~= 200 then
        kong.log.err("failed to verify access token: ", res.status)
        return kong.response.exit(401)
    end

    -- res.body is a JSON string with the following structure:
    -- {
    --     "sub": "123456789",
    --     "name": "John Doe",
    --     "email": "a@a.com"
    -- }
    local info = cjson.decode(res.body)
    return info
end

function AuthenticationHandler:access(conf)
    local access_token = kong.request.get_headers()[conf.token_header]

    if not access_token then
        return true
    end

    access_token = access_token:sub(8, -1)

    verify_access_token(conf, access_token)
    
    local user_id = get_access_token_info(conf, access_token).sub
    kong.service.request.set_header("x-user-id", user_id)
    kong.response.set_header("x-user-id", user_id)

    return true
end

return AuthenticationHandler
