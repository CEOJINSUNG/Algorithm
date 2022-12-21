class ArrayQueue
    attr_accessor :queue

    def initialize(queue = [])
        @queue = queue
    end

    def add(item)
        queue.unshift(item)
    end

    def pop
        queue.pop
    end

    def peek
        queue[-1]
    end
end

queue = ArrayQueue.new
queue.add(3)
queue.add(4)
queue.add(5)

puts queue.inspect()
queue.pop
puts queue.inspect()
puts queue.peek

queue = Queue.new
queue << 1
queue << 2
queue << 3

puts queue.pop
puts queue.pop

queue = SizedQueue.new(5)

queue.push(:oranges)
queue.push(:apples)
queue.push(:blue)
queue.push(:orange)
queue.push(:green)

puts queue.pop
puts queue.pop
puts queue.pop
puts queue.pop
puts queue.pop