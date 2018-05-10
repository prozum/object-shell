#include <vector>
#include <json/json.h>
#include <iostream>


int main(int argc, char **argv)
{
    std::vector<char> cin_strs;
    std::streamsize buffer_sz = 65536;
    std::vector<char> buffer(buffer_sz);
    cin_strs.reserve(buffer_sz);

    auto rdbuf = std::cin.rdbuf();
    while (auto cnt_char = rdbuf->sgetn(buffer.data(), buffer_sz))
        cin_strs.insert(cin_strs.end(), buffer.data(), buffer.data() + cnt_char);

    for (auto str: cin_strs)
        std::cout << str;
}