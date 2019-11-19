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
    handle:write("true")
    data = handle:read(packet_len)
    print(data)
    str = nil
    while not str do str = io.read() end
    if str == "exit" then break end
end
handle:close()