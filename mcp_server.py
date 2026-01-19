from fastmcp import FastMCP
from data import PATIENTS, BILLS


mcp = FastMCP("Hospital MCP Server")




# -------------------- TOOLS --------------------


@mcp.tool()
def get_patient_record(patient_id: str) -> dict:
    """Fetch patient details by patient ID"""
    return PATIENTS.get(patient_id, {"error": "Patient not found"})




@mcp.tool()
def get_patient_bill(patient_id: str) -> dict:
    """Fetch billing details by patient ID"""
    return BILLS.get(patient_id, {"error": "Bill not found"})




@mcp.tool()
def list_all_patients() -> list:
    """List all registered patients"""
    return list(PATIENTS.keys())


# -------------------- SERVER START --------------------

if __name__ == "__main__":
    mcp.run()




