local internet = require("internet")
local handle = internet.open("example.com", 1337)

handle:write("1234")
handle:close()