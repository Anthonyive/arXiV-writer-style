#ifndef texfile_hpp
#define texfile_hpp

#include <stdio.h>
#include <string>
#include <fstream>

using namespace std;

class texfile {
public:
    texfile();
    texfile(const string&);
    ~texfile();
    
    // Methods
    string matchline();
   
    
    
private:
    ifstream input;
    string file_name;
};




#endif /* texfile_hpp */