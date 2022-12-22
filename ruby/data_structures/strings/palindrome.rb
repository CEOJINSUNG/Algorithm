def is_palindrome(s)
    letters_only = s.downcase.gsub(/[^0-9a-z]/i, '')
    letters_only.reverse == letters_only
end

puts is_palindrome('A man, a plan, a canal: Panama')
puts is_palindrome('race a car')
puts is_palindrome('ab_a')

def is_palindrome(s)
    letters_only_array = s.downcase.gsub(/[^0-9a-z]/i, '').split('')
    reversed_array = []
    letters_only_array.each do |letter|
        reversed_array.unshift(letter)
    end
    letters_only_array == reversed_array
end

puts is_palindrome('A man, a plan, a canal: Panama')
puts is_palindrome('race a car')
puts is_palindrome('ab_a')

def is_palindrome(s)
    letters_only = s.downcase.gsub(/[^0-9a-z]/i, '')
    p1, p2 = 0, letters_only.length - 1

    while p1 < p2
        if letters_only[p1] == letters_only[p2]
            p1 += 1
            p2 -= 1
        else
            return false
        end
    end
    true
end

puts is_palindrome('A man, a plan, a canal: Panama')
puts is_palindrome('race a car')
puts is_palindrome('ab_a')