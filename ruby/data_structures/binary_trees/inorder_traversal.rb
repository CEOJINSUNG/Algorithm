class TreeNode
    attr_accessor :val, :left, :right
    
    def initialize(val)
        @val = val
        @left, @right = nil, nil
    end
end

def inorder_traversal(root)
    ans = []
    
    def traverse(node, ans)
        unless node.nil?
            traverse(node.left, ans)
            ans.push(node.val)
            traverse(node.right, ans)
        end
    end
    traverse(root, ans)
    ans
end
