# Practise programs

## Isoceles triangle pattern

```rust
fn main() {
    let size = 20;
    for row in 1..=size {
        for column in 1..=size {
            if column <= row {
                print!("*");
            }
        }
        println!("");
    }
}

// Optimial approach
fn main() {
    let size = 20;

    for i in 1..=size {
        for _ in 1..=i {
            print!("*");
        }
        println!("");
    }
}

// X-axis inverted
fn main() {
    let size = 20;

    for i in 1..=size {
        for _ in 1..=(size - i) {
            print!(" ");
        }
        for _ in 1..(i + 1) {
            print!("*");
        }
        println!("");
    }
}

```

## Equilateral triangle

```rust
fn main() {
    let height = 20;
    for i in 1..=(height) {
        for _ in 1..=(height - i) {
            print!(" ");
        }
        for _ in 1..(i * 2) {
            print!("*");
        }
        println!("");
    }
}
```

## Diamond pattern

```rust
use std::io::{self, Write};

fn main() {
    let mut height = String::new();

    print!("Diamond height: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut height).expect("Expected input");

    let height: u32 = match height.trim().parse() {
        Ok(val) => val,
        Err(err) => {
            eprintln!("Failed to parse number - {}", err);
            return;
        }
    };

    let center = (height / 2) + 1;

    for i in 1..=center {
        for _ in 1..=(center - i + 1) {
            print!("  ");
        }
        for _ in 1..=(i * 2 - 1) {
            print!("💩");
        }
        println!("");
    }
    for i in (1..center).rev() {
        for _ in 1..=(center - i + 1) {
            print!("  ");
        }
        for _ in 1..=(i * 2 - 1) {
            print!("💩");
        }
        println!("");
    }
}

```