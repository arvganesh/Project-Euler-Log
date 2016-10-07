def isPrime(n)
    if n % 2 == 0 && n != 2
        return false
    end
    for x in 2..Math.sqrt(n)
        if n % x == 0
            return false
        end
    end
    return true
end

c = 0
for x in 2..1000000
    if isPrime(x)
        c += 1
    end
    if c == 10001
        puts x
        break
    end
end
