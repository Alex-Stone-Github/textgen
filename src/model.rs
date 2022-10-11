/*
 * LOOK_BACK * TEXT_SIZE
 * 70
 * 70
 * TEXT_SIZE
 */
use crate::constants::*;

pub struct Model {
    weight1: Vec<Vec<f64>>,
    weight2: Vec<Vec<f64>>,
    weight3: Vec<Vec<f64>>,
    bias1: Vec<f64>,
    bias2: Vec<f64>,
    bias3: Vec<f64>,
}
impl Model {
    pub fn new() -> Self {
    }
    pub fn what_is_next(&self, text: String) -> char {'a'}
    pub fn mutate_behavior(&mut self, rate: f64) {}
}



fn random_f64_vec(length: usize) -> Vec<f64> {
    (0..length).map(|x| rand::random::<f64>() as f64).collect()
}
