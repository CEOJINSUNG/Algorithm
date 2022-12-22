def remove_vowels(s)
    result_array = []
    s.downcase!

    start_array = s.split('')
    start_array.each do |letter|
        result_array.push(letter) if letter != 'a' && letter != 'e' && letter != 'i' && letter != 'o' && letter != 'u'
    end
    result_array.join('')
end

print(remove_vowels('leetcodeisacommunityforcoders'), ' ')
print(remove_vowels('aeiou'), "\n")

def remove_vowels(s)
    vowels = /[aeiou]/i
    s.gsub!(vowels, '')
    s
end

print(remove_vowels('leetcodeisacommunityforcoders'), ' ')
print(remove_vowels('aeiou'), "\n")

def remove_vowels(s)
    s.downcase.delete('aeiou')
end

print(remove_vowels('leetcodeisacommunityforcoders'))
print(remove_vowels('aeiou'))