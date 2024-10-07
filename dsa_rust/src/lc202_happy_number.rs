use std::collections::HashSet;

fn is_happy(n: i32) -> bool {
    let mut seen: HashSet<i32> = HashSet::new();
    let mut num = n;
    while num != 1 && !seen.contains(&num) {
        seen.insert(num);
        let mut temp = 0;
        while num > 0 {
            let dig = num % 10;
            temp += dig * dig;
            num = num / 10;
        }
        num = temp;
        if num == 1 {
            return true;
        }
    }
    return num == 1;
}

pub fn check_happy() {
    let n = 19;
    let result = is_happy(n);
    println!("{result}")
}

// Tests for the is_happy function
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_happy_number() {
        // 19 is a happy number
        assert!(is_happy(19));
    }

    #[test]
    fn test_unhappy_number() {
        // 2 is not a happy number
        assert!(!is_happy(2));
    }

    #[test]
    fn test_happy_number_7() {
        // 7 is a happy number
        assert!(is_happy(7));
    }

    #[test]
    fn test_unhappy_number_4() {
        // 4 is not a happy number
        assert!(!is_happy(4));
    }

    #[test]
    fn test_happy_number_large() {
        // Test with a larger happy number
        assert!(is_happy(986543210));
    }
}
