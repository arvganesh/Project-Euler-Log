def isEvenDiv(n)
    for i in 1..20
        if n % i != 0
            return false
        end
    end
    return true
end

for i in (2520..10000000000).step(20)
    if isEvenDiv(i)
        print i
        break
    end
end
