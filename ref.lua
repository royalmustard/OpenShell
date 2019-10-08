--Keeps amount of items in the Refined storage system
--Author: royalmustard
--Date: 08.10.2019

local component = require("component")
local rs = component.block_refinedstorage_grid_2

item =
{
    {stack = {name = "enderio:item_basic_capacitor"}, amount = 64},
    {name = ""}
}


while(true) do
	for i,entry in ipairs(items) do
		if(rs.hasPattern(entry.stack)) then
			local rsStack = rs.getItem(entry.stack)
			local toCraft = entry.amount
			if(rsStack ~= nil) then
				toCraft = toCraft - rsStack.size
			end
			if(toCraft > 0) then
				rs.craftItem(stack, toCraft)
			end
			else
				print("Missing pattern for: " .. stack.name)
			end
		end
		os.sleep(5)
	end
