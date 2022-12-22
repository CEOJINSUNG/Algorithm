def single_number(nums)
    result_hash = {}
    nums.each do |num|
        if result_hash[num]
            result_hash[num] += 1
        else
            result_hash[num] = 1
        end
    end

    result_hash.each do |k, v|
        return k if v == 1
    end
end

puts(single_number([2, 2, 1]))
puts(single_number([4, 1, 2, 1, 2]))
puts(single_number([1]))

def single_number(nums)
    nums.find do |num|
        nums.count(num) == 1
    end
end

puts(single_number([2, 2, 1]))
puts(single_number([4, 1, 2, 1, 2]))
puts(single_number([1]))