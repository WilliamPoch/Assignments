package CA;
/**
 * 
 * @author William Sivutha Poch 5938122
 *
 */
public class Register {
	private String regName;
	private String regVal;
	private String regCode;
	
	public Register(String rNum, String code) {
		this.regName = rNum;
		this.regVal = "0000000000000000";
		this.regCode = code;
	
	}
	public String getVal() {
		return regVal;
	}
	public void setVal(String newVal) {
		this.regVal = newVal;
	}
	public void setReg(String reg) {
		this.regName = reg;
	}
	public String getReg() {
		return this.regName;
	}
	
	public String getCode() {
		return regCode;
	}
	@Override
	public String toString() {
		return String.format("%s %s ", regName, ": ["+regVal+"]" );
	}
}

