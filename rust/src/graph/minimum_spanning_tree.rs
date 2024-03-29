use super::DisjointSetUnion;

#[derive(Debug)]
pub struct Edge {
    source: i64,
    destination: i64,
    cost: i64,
}

impl PartialEq for Edge {
    fn eq(&self, other: &Self) -> bool {
        self.source == other.source && self.destination == other.destination && self.cost == other.cost
    }
}

impl Eq for Edge {}

impl Edge {
    fn new(source: i64, destination: i64, cost: i64) -> Self {
        Self {
            source,
            destination,
            cost,
        }
    }
}

pub fn kruskal(mut edges: Vec<Edge>, number_of_vertices: i64) -> (i64, Vec<Edge>) {
    let mut dsu = DisjointSetUnion::new(number_of_vertices as usize);

    edges.sort_unstable_by(|a, b| a.cost.cmp(&b.cost));
    let mut total_cost: i64 = 0;
    let mut final_edges: Vec<Edge> = Vec::new();
    let mut merge_count: i64 = 0;
    for edge in edges.iter() {
        if merge_count >= number_of_vertices - 1 {
            break;
        }

        let source: i64 = edge.source;
        let destination: i64 = edge.destination;
        if dsu.merge(source as usize, destination as usize) < std::usize::MAX {
            merge_count += 1;
            let cost: i64 = edge.cost;
            total_cost += edge.cost;
            let final_edge: Edge = Edge::new(source, destination, cost);
            final_edges.push(final_edge);
        }
    }

    (total_cost, final_edges)
 }