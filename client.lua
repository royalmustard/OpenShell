local internet = require("internet")
print("got require")
local handle = internet.open("127.0.0.1", 42069)
print("got handle")

handle:write("1234")
handle:close()