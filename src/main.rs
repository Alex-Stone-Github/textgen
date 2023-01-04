
fn main() {
    println!("Hello, world!");
}


fn random_matrix(rows: usize, columns: usize) -> amath::Matrix {
    let elements = (0..rows*columns).map(|_| rand::random()).collect();
    amath::Matrix::new(rows, columns, elements)
}
struct Linear {
    weight: amath::Matrix,
    weight_grad: Option<amath::Matrix>,
    bias: amath::Matrix,
    bias_grad: Option<amath::Matrix>,
    x: Option<amath::Matrix>,
}
impl Linear {
    fn new(nins: usize, nouts: usize) -> Self {
        Self {
            weight: random_matrix(nouts, nins),
            weight_grad: None,
            bias: random_matrix(nouts, 1),
            bias_grad: None,
            x: None,
        }
    }
    fn forward(&mut self, x: &amath::Matrix) -> amath::Matrix {
        self.x = Some(x.clone());
        let matmul = amath::Matrix::matmul(&self.weight, x).expect("x must have
        a proper shape");
        let addition = amath::Matrix::add(&matmul, &self.bias).expect("something
        terrible has happened");
        addition
    }
    fn backward(&mut self, pgrad: &amath::Matrix) -> amath::Matrix {
    }
}
