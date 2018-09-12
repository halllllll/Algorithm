# implement insertion sort

n = gets.chomp.to_i
arr = gets.chomp.split.map(&:to_i)


def printme(a)
    puts a.join(" ")
end

def insert_sort(a, idx)
    cur = a[idx]
    j = idx-1
    loop do
        break if j<0 || a[j] < cur  # cur < a[j]だと逆順で表示
        a[j+1] = a[j]
        j -= 1
    end
    a[j+1] = cur
    return a
end

printme(arr)

(1..n-1).each do |i|
    arr = insert_sort(arr, i)
    printme(arr)
end