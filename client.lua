local internet = require("internet")
print("got require")
local handle = internet.open("127.0.0.1", 42069)
print("got handle")
handle.stream.socket.finishConnect()
lines = {}
str = io.read()
while str do
    handle:write(str)
    data = handle:read(1024)
    print(data)
    str = io.read()
end
handle:close()