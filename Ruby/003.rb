def isPrime(n)
    if n % 2 == 0 && n != 2
        return false
    end
    for i in 2..Math.sqrt(n)
        if n % i == 0
            return false
        end
    end
    return true
end

def getBigPrimeFactor(n)
    var = 0
    for i in 1..n/2
        if isPrime(i) && n % i == 0
            if i > var
                var = i
                puts var
            end
        end
    end
    return var
end
puts getBigPrimeFactor(600851475143)
