local internet = require("internet")
local handle = internet.open("127.0.0.1", 42069)

handle:write("1234")
handle:close()