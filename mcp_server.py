from fastmcp import FastMCP
from data import PATIENTS, BILLS


mcp = FastMCP("Hospital MCP Server")


# -------------------- TOOLS --------------------


@mcp.tool()
def get_patient_record(patient_id: str) -> dict:
    """Retrieve a patient's medical record by patient ID.

    This MCP tool queries the in-memory patient database and returns
    the corresponding patient details if found. If the patient ID
    does not exist, a standardized error response is returned instead.

    Args:
        patient_id (str): Unique identifier for the patient

    Returns:
        dict: A dictionary containing patient details, or an error
              message in the format:
              {"error": "Patient not found"}
    """
   
    return PATIENTS.get(patient_id, {"error": "Patient not found"})




@mcp.tool()
def get_patient_bill(patient_id: str) -> dict:
    """ Retrieve a patient's billing details by patient ID.

    This MCP tool queries the hospital billing database and returns
    the corresponding bill information for the given patient. If no
    billing record exists for the specified patient ID, a standardized
    error response is returned.

    Args:
        patient_id (str): Unique identifier for the patient

    Returns:
        dict: A dictionary containing billing details, or an error
              message in the format:
              {"error": "Bill not found"}
    """
    return BILLS.get(patient_id, {"error": "Bill not found"})




@mcp.tool()
def list_all_patients() -> list:
    """List all registered patient IDs in the hospital database.

    This MCP tool retrieves and returns a list of all patient
    identifiers currently stored in the in-memory patient registry.
    It is useful for discovering available records before querying
    individual patient details or billing information.

    Returns:
        list: A list of patient ID strings."""
    
    return list(PATIENTS.keys())


# -------------------- SERVER START --------------------

if __name__ == "__main__":
    mcp.run()




