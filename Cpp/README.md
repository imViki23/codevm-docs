# C++ Tutorial

- C++ is a compile language, the source text has to be processed by a compiler producing object files, which are then combined by a linker yielding an executable program.

## Quick bites

```c++
int a = 7.2; // a becomes 7
int a {7.2}; // error: floating point to integer conversion
```

## Pointers

Pointers in C++ are variables that store the memory address of another variable.

### 1. Declaring a pointer

A pointer is declared with an asterisk **\*** before the variable name.

```c++
int *ptr;
```

### 2. Assigning a Memory Address to a Pointer

Use the address-of operator **&** to assign the address of a variable to a pointer

```c++
int a = 5;
int *ptr = &a;       // Pointer to an integer i.e. Assigning address of 'a' to pointer ptr
```

### 3. Dereferencing a Pointer

The dereference operator * is used to access the value at the memory address stored in the pointer.

```c++
cout << *ptr << "\n"; // Dereferencing pointer will retrieve value, Prints 5
```

### 4. Pointer Arithmetic

Pointers can be incremented or decremented to move to the next or previous memory location (useful in arrays).

```c++
int arr[5] = {91, 92, 93, 94, 95};

int *ptr = arr;      // ptr points to first element of array arr
cout << *ptr << ","; // Prints 91
ptr++;               // Points to next element
cout << *ptr << ","; // Prints 92
ptr++;               // Points to next element
cout << *ptr << ","; // Prints 93
ptr++;               // Points to next element
cout << *ptr << ","; // Prints 94
ptr++;               // Points to next element
cout << *ptr;        // Prints 95
```

### 5. Dynamic memory allocation

Pointers are often used with **new** and **delete** to allocate and deallocate memory at runtime.

```c++
int *ptr = new int;
*ptr = 25;
cout << *ptr;
delete ptr;
```

### 6. Pointers as reference

A pointer is useful to pass large amounts of data at low cost, instead of copying the data and pass it to other function variable, only the address is shared which points to original object, so changing value inside another function will modify original object itself.

#### Simple datatype example

```c++
void update_by_value(int another_raw)
{
    cout << "Address of another_raw = " << &another_raw << "\n"; // Outputs 0x7ffcb48324fc, different from original 'a'
    another_raw = 6;                                             // This update not going to impact original 'a'
}

void update_by_reference(int *another_ptr)
{
    cout << "Address of another_ptr = " << another_ptr << "\n"; // Outputs 0x7ffcb4832514, same as original 'a'
    *another_ptr = 6;                                           // Update value as 6 in that address
}

int main()
{
    int a = 5;
    cout << "Address of a = " << &a << "\n"; // Outputs 0x7ffcb4832514
    update_by_value(a);                      // 'a' value is copied and passed to update_by_value function
    cout << "Value of a = " << a << "\n";    // Prints 5, no changes
    update_by_reference(&a);                 // a is not copied, instead address of a is passed as reference
    cout << "Value of a = " << a << "\n";    // Prints 6
}
```