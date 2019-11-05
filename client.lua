local internet = require("internet")
print("got require")
local handle = internet.open("127.0.0.1", 42069)
print("got handle")
handle.stream.socket.finishConnect()
lines = {}
str = io.read()
while str do
    handle:write(str)
    data = handle:read(8)
    packet_len = tonumber(string.match(data, "%d+"))
    hande:write("true")
    data = handle:read(packet_len)
    print(data)
    while not str do str = io.read() end
end
handle:close()