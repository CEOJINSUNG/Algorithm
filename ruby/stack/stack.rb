# 루비 접근자와 생성자에 대하여
class Person
    def initialize(name)
        @name = name
    end

    def name() # 접근자
        @name = name
    end

    def name(value) # 설정자
        @name = value
    end
end

class Person
    attr_accessor :name # 자동으로 접근자 설정자가 생성이 됨

    def initialize(name)
        @name = name
    end
end

class StackOverflowError < StandardError; end

class Stack
    def initialize(limit, stack = [])
        @stack = stack
        @limit = limit
    end
    
    attr_accessor :stack, :limit

    def push(item)
        raise StackOverflowError unless stack.count < limit
        stack << item
    end

    def pop
        stack.pop
    end

    def peek
        stack.last
    end

    def empty?
        stack.count.zero?
    end

    def full?
        stack.count == limit
    end

    def size
        stack.count
    end

    def contains?(item)
        stack.include?(item)
    end
end

stack = Stack.new(10, [])

puts stack.empty?

stack.push(3)
stack.push(5)
stack.push(7)
stack.push(9)

puts stack.full?
puts stack.contains?(5)
puts stack.pop
puts stack.peek
puts stack.size
puts stack.inspect

stack.push(13)
stack.push(15)
stack.push(17)
stack.push(19)
stack.push(23)
stack.push(25)
stack.push(27)
stack.push(29)

