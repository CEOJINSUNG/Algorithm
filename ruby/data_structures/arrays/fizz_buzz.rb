def fizz_buzz(n)
    str = []

    # n이 5이면 do에서 0, 1, 2, 3, 4 가 나옴
    n.times do |i|
        i += 1

        if i % 5 == 0 && i % 3 == 0
            str.push("FizzBuzz")
        elsif i % 3 == 0
            str.push("Fizz")
        elsif i % 5 == 0
            str.push("Buzz")
        else
            str.push(i.to_s)
        end
    end
    return str
end

n = 15
puts fizz_buzz(n)

def fizz_buzz(n)
    str = []
    
    (0...n).each do |i|
        i += 1
        num_str = ''

        num_str += 'Fizz' if i % 3 == 0
        num_str += 'Buzz' if i % 5 == 0

        num_str = i.to_s if num_str == ''

        str.push(num_str)
    end
    return str
end

n = 15
puts fizz_buzz(n)