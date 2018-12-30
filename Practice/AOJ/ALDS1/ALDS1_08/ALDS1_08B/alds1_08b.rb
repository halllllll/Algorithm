n = gets.chomp.to_i
Node = Struct.new(:num, :parent, :left, :right)

class BinSearchTree
  attr_accessor :root
  def initialize
    @root = nil
  end

  def inorder(r, order)
    if r.nil?.!
      inorder(r.left, order)
      order << r.num
      inorder(r.right, order)
    end
  end
  
  def preorder(r, order)
    if r.nil?.!
      order << r.num
      preorder(r.left, order)
      preorder(r.right, order)
    end
  end
  
  def find(k)
    x = @root
    flag = false
    until x.nil?
      if k == x.num
        flag = true
        break
      elsif k < x.num
        x = x.left
      elsif x.num < k
        x = x.right      
      end
    end
    flag
  end

  def insert(k)
    x = @root
    y = nil
    z = Node.new
    z.num = k
    until x.nil?
      y = x
      if z.num < x.num
        x = x.left
      else
        x = x.right
      end
    end
    z.parent = y
    if y.nil?
      @root = z
    else
      if z.num < y.num
        y.left = z
      else
        y.right = z
      end
    end
  end
end

bst = BinSearchTree.new

n.times do
  cmd, i = gets.chomp.split.map{|t| t.match?(/\d/) ? t.to_i : t}
  case cmd
  when "insert"
    bst.insert(i)
  when "print"
    root = bst.root
    in_res, pre_res = [], []
    bst.inorder(root, in_res)
    puts " " + in_res.map(&:to_s).join(' ')
    bst.preorder(root, pre_res)
    puts " " + pre_res.map(&:to_s).join(' ')
  when "find"
    puts bst.find(i) ? "yes" : "no"
  end
end