sum = 0
num = 0
num2 = 1
for i in 1...33
    temp = num + num2
    num = num2
    num2 = temp
    if temp % 2 == 0
        sum += temp
    end
end
puts sum
