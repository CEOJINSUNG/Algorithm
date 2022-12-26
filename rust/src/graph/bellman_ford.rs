use std::collections::BTreeMap;
use std::ops::{Add, Neg, Sub};

type Graph<V, E> = BTreeMap<V, BTreeMap<V, E>>;

pub fn bellman_ford<
    V: Ord + Copy,
    E: Ord + Copy + Add<Output = E> + Neg<Output = E> + Sub<Output = E>
>(
    graph: &Graph<V, E>,
    start: &V,
) -> Option<BTreeMap<V, Option<(V, E)>>> {
    let mut ans: BTreeMap<V, Option<(V, E)>> = BTreeMap::new();

    ans.insert(*start, None);

    for _ in 1..(graph.len()) {
        for (u, edges) in graph {
            let dist_u = match ans.get(u) {
                Some(Some((_, d))) => Some(*d),
                Some(None) => None,
                None => continue,
            };

            for (v, d) in edges {
                match ans.get(v) {
                    Some(Some((_, dist)))
                        if match dist_u {
                            Some(dist_u) => dist_u + *d >= *dist,
                            None => d >= dist,
                        } => {}
                    Some(None) => {
                        match dist_u {
                            Some(dist_u) if dist_u >= -*d => {}
                            _ => {
                                if *d > *d + *d {
                                    return None;
                                }
                            }
                        }
                    }
                    _ => {
                        ans.insert(*v, Some((*u, match dist_u {
                            Some(dist) => dist + *d,
                            None => *d,
                        })))
                    }

                }
            }
        }
    }

    for (u, edges) in graph {
        for (v, d) in edges {
            match (ans.get(u), ans.get(v)) {
                (Some(None), Some(None)) if *d > *d + *d => return None,
                (Some(None), Some(Some((_, dv)))) if d < dv => return None,
                (Some(Some((_, du))), Some(None)) if *du < -*d => return None,
                (Some(Some((_, du))), Some(Some((_, dv)))) if *du + *d < *dv => return None,
                (_, _) => {}
            }
        }
    }

    Some(ans)
}