#include "texfile.hpp"

#include <iostream>
#include <sstream>
#include <string>

using namespace std;

texfile::texfile() {}

texfile::texfile(const string& name): file_name(name) {
    input.open(file_name);
    if (!input.is_open()) {
        cout << "Fail to open " << file_name << endl;
    }
}

texfile::~texfile() {
    input.close();
    delete this;
}

texfile::matchline() {
	string line;
	getline(input_data, line);
}