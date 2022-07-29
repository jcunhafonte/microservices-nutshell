local http = require "resty.http"

local AuthenticationHandler = {
    VERSION = "1.0",
    PRIORITY = 1000,
}

local function verify_access_token(conf, access_token)
    local httpc = http:new()
    local headers = {
        ["Authorization"] = "Bearer " .. access_token,
    }

    local res, err = httpc:request_uri(conf.authentication_endpoint, {
        method = "GET",
        ssl_verify = false,
        headers = headers,
    })

    if not res then
        kong.log.err("failed to reach authentication endpoint: ", err)
        return kong.response.exit(500)
    end
    
    -- if request is unauthorized return error
    if res.status ~= 200 then
        kong.log.err("failed to verify access token: ", res.status)
        return kong.response.exit(401)
    end

    return true -- all is well
end

function AuthenticationHandler:access(conf)
    local access_token = kong.request.get_headers()[conf.token_header]

    if not access_token then
        kong.log.err("no access token found in request")
        return kong.response.exit(401)
    end

    -- replace Bearer prefix
    access_token = access_token:sub(8, -1) -- drop "Bearer "
    verify_access_token(conf, access_token)

    -- all is well, continue with the request
    return true
end

return AuthenticationHandler
