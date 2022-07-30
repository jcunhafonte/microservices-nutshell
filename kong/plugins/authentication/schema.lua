local typedefs = require "kong.db.schema.typedefs"

return {
    name = "authentication",
    fields = {
        { protocols = typedefs.protocols_http },
        { consumer = typedefs.no_consumer },
        { config = {
            type = "record",
            fields = {
                { authentication_verify_endpoint = typedefs.url({ required = true }) },
                { authentication_info_endpoint = typedefs.url({ required = true }) },
                { token_header = typedefs.header_name { default = "Authorization", required = true }, }
            },
        }, },
    },
}
