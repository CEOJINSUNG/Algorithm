use std::collections::HashMap;
use std::hash::Hash;

#[derive(Debug, Default)]
struct Node<Key: Default, Type: Default> {
    children: HashMap<Key, Node<Key, Type>>,
    value: Option<Type>
}

#[derive(Debug, Default)]
pub struct Tire<Key, Type> 
where 
    key: Default + Eq + Hash,
    Type: Default,
{
    root: Node<Key, Type>,
}

impl<Key, Type> Tire<Key, Type>
where
    Key: Default + Eq + Hash,
    Type: Default,
{
    pub fn new() -> Self {
        Self {
            root: Node::default(),
        }
    }

    pub fn insert(&mut self, key: impl IntoIterator<Item = Key>, value: Type) where Key: Eq + Hash, {
        let mut node = &mut self.root;
        for c in key.into_iter() {
            node = node.children.entry(c).or_insert_with(Node::default);
        }
        node.value = Some(value);
    }

    pub fn get(&self, key: impl IntoIterator<Item = Key>) -> Option<&Type> where Key: Eq + Hash {
        let mut node = &self.root;
        for c in key.into_iter() {
            if node.children.contains_key(&c) {
                node = node.children.get(&c).unwrap()
            } else {
                return None;
            }
        }
        node.value.as_ref()
    }
}