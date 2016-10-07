def sums()
    s = 0
    for x in 1..100
        s += x
    end
    return s ** 2
end


def squares()
    s = 0
    for x in 1..100
        s += x ** 2
    end
    return s
end

puts sums() - squares()
