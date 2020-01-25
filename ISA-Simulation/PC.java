package CA;
/**
 * 
 * @author William Sivutha Poch 5938122
 *
 */
public class PC {
	private String inputs;
	private int pc;
	private String encoded;
	private int clockcycle;
	private String result;
	private String reg;
	private int num;
	private String re;
	private int rm;
	
	public String getRe() {
		return re;
	}

	public void setRe(String re) {
		this.re = re;
	}

	public int getRm() {
		return rm;
	}

	public void setRm(int rm) {
		this.rm = rm;
	}

	public PC() {
		this.inputs = null;
		this.pc = 0;
		this.encoded = null;
		this.re = null;
		this.rm = 0;
	}
	
	public String getReg() {
		return reg;
	}

	public void setReg(String reg) {
		this.reg = reg;
	}

	public int getNum() {
		return num;
	}

	public void setNum(int num) {
		this.num = num;
	}

	public String getResult() {
		return result;
	}

	public void setResult(String result) {
		this.result = result;
	}
	
	public void push(String in, int pc, String encoded, int clockcycle) {
		this.inputs = in;
		this.pc = pc;
		this.encoded = encoded;
		this.clockcycle = clockcycle;
		this.re = null;
		this.rm = 0;
	}
	
	public String pop() {
		return this.inputs;
	}
	
	public String getInputs() {
		return inputs;
	}

	public void setInputs(String inputs) {
		this.inputs = inputs;
	}

	public int getPc() {
		return pc;
	}

	public void setPc(int pc) {
		this.pc = pc;
	}

	public String getEncoded() {
		return encoded;
	}

	public void setEncoded(String encoded) {
		this.encoded = encoded;
	}

	public int getClockcycle() {
		return clockcycle;
	}

	public void setClockcycle(int clockcycle) {
		this.clockcycle = clockcycle;
	}

	@Override
	public String toString() {
		return String.format("%-3s %15s %37s %20s ", "PC["+pc+"]", inputs, encoded, clockcycle );
	}
	
	public String stepOfReg() {
		if (re != null) {
			return String.format("%s = %s %s %s", getReg(),"["+getNum()+"]", "["+getResult()+"]", "RE : "+getRe());
		} else if (rm != 0) {
			return String.format("%s %s = %s %s","RM : ", getReg(),"["+getNum()+"]", "["+getResult()+"]");
		}
		return String.format("%s = %s %s", getReg(),"["+getNum()+"]", "["+getResult()+"]");
	}
	
}
