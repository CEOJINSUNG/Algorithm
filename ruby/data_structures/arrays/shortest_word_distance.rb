def shortest_distance(words, word1, word2)
    return 0 if word1 == word2
    return 0 unless words.include?(word1) && words.include?(word2)

    minimum_distance = words.length
    words.each_with_index do |out, out_index|
        words.each_with_index do |inner, inner_index|
            if ((inner == word1 && out == word2) || (inner == word2 && out == word1) && (minimum_distance > (out_index - inner_index).abs))
                minimum_distance = (out_index - inner_index).abs
            end
        end
    end
    minimum_distance
end

words = %w[practice makes perfect coding makes]
word1 = 'coding'
word2 = 'practice'
print(shortest_distance(words, word1, word2))

words = %w[practice makes perfect coding makes]
word1 = 'makes'
word2 = 'coding'
puts(shortest_distance(words, word1, word2))