def isPal(n)
    s = n.to_s
    if s == s.reverse()
        return true
    end
    return false
end

def pal()
    bign = 0
    for x in 1000.downto(100)
        for y in 1000.downto(100)
            pr = x * y
            if isPal(pr)
                if pr > bign
                    bign = pr
                end
            end
        end
    end
    return bign
end
puts pal
