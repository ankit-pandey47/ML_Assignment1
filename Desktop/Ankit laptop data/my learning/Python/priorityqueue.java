import java.util.*;
public class priorityqueue{
    public static void main(String[] args) {
         
        //usinf reverseorder inside pq means it give priority to max elemtn more
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        pq.add(12);
        pq.add(23);
        pq.add(11);

        System.out.println(pq.remove());
    }
}