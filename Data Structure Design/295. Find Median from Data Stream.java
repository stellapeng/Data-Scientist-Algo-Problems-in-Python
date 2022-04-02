// PQ is implemented by heap
// in python, there's a heapq library


class MedianFinder {
    private PriorityQueue<Integer> large;
    private PriorityQueue<Integer> small;

    public MedianFinder() {
        large = new PriorityQueue<>(); // min PQ by default
        small = new PriorityQueue<>(Collections.reverseOrder()); // max PQ
    }
    
    public void addNum(int num) {
        if (large.size() >= small.size()){
            large.offer(num);
            small.offer(large.poll());
        }else{
            small.offer(num);
            large.offer(small.poll());
        }
    }
    
    public double findMedian() {
        if (large.size() > small.size()){
            return large.peek();
        }  
        else if (large.size() < small.size()){
            return small.peek();
        }   
        else{
            return (large.peek() + small.peek())/2.0;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */