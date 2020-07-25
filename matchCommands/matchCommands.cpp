#include <stdio.h>
#include "texfile.hpp"
#include <string>
#include <iostream>

using namespace std;

int main() {
	string download_path = "../Download/";
	string targz_path = download_path + "targz/";
	string unzipped_path = download_path + "unzipped/";
    
    const string categories[32] = { "math.AC-CommutativeAlgebra", "math.AG-AlgebraicGeometry", "math.AP-AnalysisofPDEs", 
    "math.AT-AlgebraicTopology", "math.CA-ClassicalAnalysisandODEs", "math.CO-Combinatorics", "math.CT-CategoryTheory", 
    "math.CV-ComplexVariables", "math.DG-DifferentialGeometry", "math.DS-DynamicalSystems", "math.FA-FunctionalAnalysis", 
    "math.GM-GeneralMathematics", "math.GN-GeneralTopology", "math.GR-GroupTheory", "math.GT-GeometricTopology", 
    "math.HO-HistoryandOverview", "math.IT-InformationTheory", "math.KT-K-TheoryandHomology", "math.LO-Logic", 
    "math.MG-MetricGeometry", "math.MP-MathematicalPhysics", "math.NA-NumericalAnalysis", "math.NT-NumberTheory", 
    "math.OA-OperatorAlgebras", "math.OC-OptimizationandControl", "math.PR-Probability", "math.QA-QuantumAlgebra", 
    "math.RA-RingsandAlgebras", "math.RT-RepresentationTheory", "math.SG-SymplecticGeometry", "math.SP-SpectralTheory", "math.ST-StatisticsTheory"}; 

    for (int i = 0; i < 32; i++) {
    	cout << categories[i] << "\n"; 
    }


	// texfile* file1 = new texfile(file1name);
	return 0;
}