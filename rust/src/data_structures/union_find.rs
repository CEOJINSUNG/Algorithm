pub struct UnionFind {
    id: Vec<usize>,
    size: Vec<usize>,
    count: usize
}

impl UnionFind {
    pub fn new(n: usize) -> Self {
        let mut id = vec![0; n];
        let mut size = vec![0; n];
        for i in 0..n {
            id[i] = i;
            size[i] = 1;
        }

        Self { id, size, count: n }
    }

    pub fn find(&mut self, x: usize) -> usize {
        let mut x = x;
        while x != self.id[x] {
            x = self.id[x];
        }
        x
    }

    pub fn union(&mut self, x: usize, y: usize) -> bool {
        let x = self.find(x);
        let y = self.find(y);
        
        if x == y {
            return false;
        }

        if self.size[x] < self.size[y] {
            self.id[x] = y;
            self.size[y] += self.size[x];
        } else {
            self.id[y] = x;
            self.size[x] += self.size[y];
        }
        self.count -= 1;
        true
    }

    pub fn is_same_set(&mut self, x: usize, y: usize) -> bool {
        self.find(x) == self.find(y)
    }

    pub fn count(&self) -> usize {
        self.count
    }
}