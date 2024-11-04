# Rust tutorial

## Table of contents

- [Quick Bites](#quick-bites)
- [Cheatsheets](#cheatsheets)
- [Rust sample program](#rust-sample-program)
- [Concepts](#concepts)
    - [1. Variables](#1-variables)
    - [2. Data types](#2-data-types)
    - [3. Functions](#3-functions)
    - [4. Ownership](#4-ownership)
    - [5. Conditional statements and Loops](#5-condtional-statements-and-loops)
    - [6. Structs](#6-structs)
    - [7. Enum & pattern matching](#7-enum--pattern-matching)

## Quick Bites

- Rust is an alternative to C++.
- It is memory safe.
- It has no concept of NULL.
- It follows Ownership and borrow concept, so it doesn't need garbage collector, hence it is memory safe.
    - [Heap memory variables can only be moved, copy is not possible.](#heap-variables-can-only-be-moved-copy-is-not-possible)
    - [For heap variable, there can be only one owner.](#for-heap-variable-there-can-be-only-one-owner) 
    - [Local heap variables cannot be returned as reference, as it is descoped.](#local-heap-variables-cannot-be-returned-as-reference-as-it-is-descoped)
- Use underscore if the variable is not used.
- **cargo** is a package manager and build tool for rust.

## Cheatsheets

- `rustc --version` - To check rust version installed.
- `cargo --version` - To check cargo version installed.
- `cargo new rust_app` - To create new rust application.
- `cargo run` - To run rust app.
- `cargo build` - To build rust app to executable.

## Rust sample program

Below is a number guessing game sample program.

```rust
use std::{
    cmp::Ordering,
    io::{self, Write},
};

use colored::Colorize;
use rand::Rng;

fn main() {
    println!("!!!!!!!!!!!!!!!!!! Guessing Game !!!!!!!!!!!!!!!!!!");

    let secret_number = rand::thread_rng().gen_range(1, 11);
    println!("Secret number = {}", secret_number);

    loop {
        print!("Guess a number: ");
        io::stdout().flush().unwrap();

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("No input from user");

        let guess: u32 = match guess.trim().parse() {
            Result::Ok(num) => num,
            Result::Err(_) => continue,
        };

        match guess.cmp(&secret_number) {
            Ordering::Equal => {
                println!("{}", "Guessed correct".green());
                break;
            }
            Ordering::Less => println!("{}", "Too low".red()),
            Ordering::Greater => println!("{}", "Too high".red()),
        }
    }
}
```

## Concepts

### 1. Variables

#### Variables are immutable by default

```rust
let x = 5;
x = 6; // Compile error: cannot assign again to a immutable variable
```

#### Use `mut` to make variables mutable

```rust
let mut x = 5;
x = 6; // No error
```

#### Shadowing

- We can't mutate but we can shadow variable.

```rust
let x = 5;
println!("x = {}", x); // Outputs x = 5
let x = 6;
println!("x = {}", x);  // Outputs x = 6
```

```rust
let x = 5;
println!("x = {}", x); // Outputs x = 5
let x = "hello";
println!("x = {}", x);  // Outputs x = hello
```

#### Constant variable

- Type is mandatory for const.
- Once assigned it can't be changed or mutated.

```rust
const SEQ_MAX: u32 = 5;
println!("x = {}", SEQ_MAX); // Outputs x = 5
```

### 2. Data types

#### Scalar data type

```rust
let x: u32 = 800_000; // Outputs 800000
let x: f64 = 4.3 + 3.3; // Outputs 7.6
let x: bool = true; // Outputs true
let x: char = 'S'; // Outputs S
```

#### Complex data type - Arrays and Tuples

```rust
let arr = [99, 98, 97];
println!("{}", arr[2]); // Outputs 97

let tup = ("Viki", 294);
let (_name, rank) = tup;
println!("{} and {}", tup.1, rank); // Outputs 294 and 294
```

### 3. Functions

```rust
fn main() {
    let result = add(1, 3);
    println!("{}", result); // Outputs 4
}

fn add(a: i32, b: i32) -> i32 {
    return a + b;
}
```

### 4. Ownership

#### Heap variables can only be moved, copy is not possible.

```rust
// Stack memory variable
let a = "hello";
let b = a;
println!("a = {}, b = {}", a, b); // Ouputs a = hello, b = hello as copy is allowed

// BUT
let a = String::from("hello");
let b = a;
println!("a = {}, b = {}", a, b); // Will throw value borrowed here after move error

// Reason is because "hello" is a fixed size data which gets stored in stack memory,
// and can be copied to variable b, but String::from("hello") is dynamic sized, 
// so it gets stored in heap memory. And heap memory (or dynamic sized memory) 
// variables cannot be simply assigned to other variable. But if you still want do clone

let a = String::from("hello");
let b = a.clone();
println!("a = {}, b = {}", a, b); // Ouputs a = hello, b = hello
```

#### For heap variable, there can be only one owner

```rust
fn main() {
    let mut a = String::from("hello");
    echo(a);
    let b = a.push_str("world"); // Throws value borrowed here after move error, because a is moved or descoped
}

fn echo(msg: String) {
    // Reference of "a" is not passed here, so msg become owner of String::from("hello") and "a" become descoped
    println!("echo msg = {}", msg);
}
```

So how to access value of a without taking ownership ? Pass reference like below.

```rust
fn main() {
    let mut a = String::from("hello");
    echo(&mut a);
    a.push_str("world");
    println!("a = {}", a); // Outputs helloworld
}

fn echo(msg: &mut String) {
    println!("echo msg = {}", msg);
}
```

#### Local heap variables cannot be returned as reference, as it is descoped

```rust
fn main() {
    let a = greet();
    println!("a = {}", a);
}

fn greet() -> &String {
    let msg = String::from("hello");
    &msg // Throws cannot return reference to local variable msg, i.e. because a will be descoped
}
```

So, then how to return heap variables from a function ? Transfer ownership

```rust
fn main() {
    let a: String = greet(); // a get ownership of String::from("hello") from greet function
    println!("a = {}", a);
}

fn greet() -> String {
    let msg = String::from("hello");
    msg
}
```

### 5. Condtional statements and loops

### 6. Structs

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn create_square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }
}

fn main() {
    let a = Rectangle {
        width: 10,
        height: 50,
    };
    println!("Area of a = {}", a.area()); // Outputs Area of a = 500
    let b = Rectangle::create_square(25); // :: similar to accessing static in java
    println!("Area of b = {}", b.area()); // Outputs Area of b = 625
}

```

### 7. Enum & pattern matching

```rust
enum Color {
    Red,
    Green,
    Blue,
}

fn main() {
    let red_color = Color::Red;
    println!("HEX = {}", get_hex(&red_color));
}

fn get_hex(color: &Color) -> &str {
    match color {
        Color::Red => "#F00",
        Color::Blue => "#0F0",
        Color::Green => "#00F",
    }
}
```

```rust
enum Color {
    Red(String),
    Green(String),
    Blue(String),
}

fn main() {
    let red_color = Color::Red(String::from("#F00"));
    println!("HEX = {:#?}", get_hex(&red_color));
}

fn get_hex(color: &Color) -> &String {
    match color {
        Color::Red(hex) => hex,
        Color::Blue(hex) => hex,
        Color::Green(hex) => hex,
    }
}
```