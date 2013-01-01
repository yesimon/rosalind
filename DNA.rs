extern mod std;
use std::map;
use std::map::Map;
use std::map::HashMap;


fn main() {
    let s: ~str = (io::stdin() as io::ReaderUtil).read_line();
    let t: Map<char,int> = HashMap::<char,int>() as Map::<char,int>;
    t.insert('A', 0);
    t.insert('C', 0);
    t.insert('G', 0);
    t.insert('T', 0);
    for str::chars_each(s) |c| {
        let count: int = t.get(c);
        t.insert(c, count + 1);
    }
    io::println(fmt!("%d %d %d %d", t.get('A'), t.get('C'), t.get('G'), t.get('T')));
}
