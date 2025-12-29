import java.util.ArrayList;
import java.util.Stack;
class MinStack {
    public Stack<Integer> stack;
    public ArrayList<Integer> mins;
    public MinStack() {
        this.stack = new Stack<>();
        this.mins = new ArrayList<>();
    }

    public void push(int val) {
        if (mins.isEmpty())
            this.mins.add(val);
        else {
            int curr_min = this.mins.getLast();
            if (val <= curr_min)
                this.mins.add(val);
        }
        this.stack.push(val);
    }

    public void pop() {
        if (this.stack.isEmpty()) return;
        if (!this.mins.isEmpty()) {
            int top = this.stack.peek();
            int curr_min = this.mins.getLast();
            if (top == curr_min)
                this.mins.removeLast();
        }
        this.stack.pop();
    }
    public int top() {
        if (this.stack.isEmpty()) return -1;
        return this.stack.peek();
    }
    public int getMin() {
        if (this.mins.isEmpty()) return -1;
        return this.mins.getLast();
    }
}
