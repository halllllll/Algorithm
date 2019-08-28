# greatest common divisor, by euclid algoryhm
a, b = gets.chomp.split.map(&:to_i)

def gcd(a, b)
    a, b = a > b ? gcd(b, a) : a, b
    loop do
        break if a<1
        a, b = b%a, a
    end
    b
end

puts gcd(a, b)