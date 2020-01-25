package CA;

/**
 * 
 * @author William Sivutha Poch 5938122
 *
 */
import java.util.ArrayList;
import java.util.Scanner;

public class Driver {

	public static void sim(ArrayList<Register> registers, ArrayList<PC> pc) {
		Scanner in = new Scanner(System.in);
		int counter = 0;
		int start = 1;
		while (start != 0) {
			String input = in.nextLine();
			String parts[] = input.split(" ");
			String command = parts[0];
			String op1 = parts[1];
			String op2 = parts[2];
			if (command.equals("mov")) {
				mov(registers, pc, op1, op2, counter);
				counter++;
			} else if (command.equals("add")) {
				add(registers, pc, op1, op2, counter);
				counter++;
			} else if (command.equals("sub")) {
				sub(registers, pc, op1, op2, counter);
				counter++;
			} else if (command.equals("mul")) {
				mul(registers, pc, op1, op2, counter);
				counter++;
			} else if (command.equals("div")) {
				div(registers, pc, op1, op2, counter);
				counter++;
			} else if (command.equals("end")) {
				end(registers, pc);
				start = 0;
			} else {
				System.out.println("Invalid input.");
			}
		}
		in.close();
	}

	public static void main(String[] args) {
		ArrayList<Register> registers = new ArrayList<Register>();
		Register r0 = new Register("r0", "000");
		Register r1 = new Register("r1", "001");
		Register r2 = new Register("r2", "010");
		Register r3 = new Register("r3", "011");
		Register r4 = new Register("r4", "100");
		Register r5 = new Register("r5", "101");
		Register r6 = new Register("r6", "110");
		Register r7 = new Register("r7", "111");
		registers.add(r0);
		registers.add(r1);
		registers.add(r2);
		registers.add(r3);
		registers.add(r4);
		registers.add(r5);
		registers.add(r6);
		registers.add(r7);
		ArrayList<PC> pc = new ArrayList<PC>();
		System.out.println("Input Commands: ");
		System.out.println("Opcode : mov, add, sub, ,mul, div");
		System.out.println("Operand 1: R0 - R7");
		System.out.println("Operand 2: R0 - R7 or decimal value");
		System.out.println("Input command followed by operand 1 and operand 2:");
		System.out.println("'end 0 0 ' stops the program.");
		sim(registers, pc);

	}

	public static boolean check(ArrayList<Register> registers, String op) {
		for (Register r : registers) {
			if (r.getReg().equals(op)) {
				return true;
			}
		}
		return false;
	}

	public static String toBinaryMul(String num) {
		int bin = Integer.parseInt(num);
		if (bin < 0) {
			return Integer.toBinaryString(bin);
		}
		return String.format("%032d", Integer.parseInt(Integer.toBinaryString(bin)));
	}

	public static String toBinary(String num) {
		int bin = Integer.parseInt(num);
		if (bin < 0) {
			String result = Integer.toBinaryString(bin);
			if (result.length() > 16) {
				result = result.substring(result.length() - 16);
			}
			return result;
		}
		return String.format("%016d", Integer.parseInt(Integer.toBinaryString(bin)));
	}

	public static String invert(String bin) {
		String result = bin;
		result = result.replace("0", " ");
		result = result.replace("1", "0");
		result = result.replace(" ", "1");
		return result;
	}

	public static int toInt(String num) {
		if (num.charAt(0) == '1') {
			String inverted = invert(num);
			int decVal = Integer.parseInt(inverted, 2);
			decVal = (decVal + 1) * -1;
			return decVal;
		} else {
			long l = Long.parseLong(num, 2);
			int i = (int) l;
			return i;
		}
	}

	public static void end(ArrayList<Register> registers, ArrayList<PC> pc) {
		System.out.println(String.format("%3s %15s %40s %25s ", "PC", "Decoded", "Encoded instructions(24-bit): ",
				"Clock Cycles"));
		for (PC pcs : pc) {
			System.out.println(pcs.toString());
		}
		System.out.println();
		System.out.println(" Step of Register ");
		for (PC p : pc) {
			System.out.println(p.stepOfReg());
		}
		System.out.println();
		System.out.println(" CPI of the program");
		int clock = 0;
		int counter = 0;
		for (PC a : pc) {
			counter++;
			clock += a.getClockcycle();
		}
		System.out.println((float) clock / counter);
		System.out.println();
		System.out.println("Final Registers");
		for (Register b : registers) {
			System.out.println(b.toString());
		}

	}

	public static void add(ArrayList<Register> registers, ArrayList<PC> pc, String op1, String op2, int counter) {
		String input = "add " + op1 + " " + op2;
		PC ins = new PC();
		if (check(registers, op2) == true) {
			for (Register reg2 : registers) {
				if (reg2.getReg().equals(op2)) {
					for (Register reg1 : registers) {
						if (reg1.getReg().equals(op1)) {
							String val = toBinary(Integer.toString((toInt(reg1.getVal()) + toInt(reg2.getVal()))));
							reg1.setVal(val);
							String encoded = "00010 " + reg1.getCode() + " "
									+ toBinary(Integer.toString((toInt(reg2.getVal()))));
							ins.push(input, counter, encoded, 2);
							ins.setResult(val);
							ins.setNum(toInt(val));
							ins.setReg(reg1.getReg());
						}
					}
				}

			}
		} else {
			String value = toBinary(op2);
			for (Register reg1 : registers) {
				if (reg1.getReg().equals(op1)) {
					String val = toBinary(Integer.toString((toInt(reg1.getVal()) + toInt(value))));
					reg1.setVal(val);
					String encoded = "00010 " + reg1.getCode() + " " + toBinary(Integer.toString((toInt(value))));
					ins.push(input, counter, encoded, 2);
					ins.setResult(val);
					ins.setNum(toInt(val));
					ins.setReg(reg1.getReg());
				}
			}

		}
		pc.add(ins);
	}

	public static void sub(ArrayList<Register> registers, ArrayList<PC> pc, String op1, String op2, int counter) {
		String input = "sub " + op1 + " " + op2;
		PC ins = new PC();
		if (check(registers, op2) == true) {
			for (Register reg2 : registers) {
				if (reg2.getReg().equals(op2)) {
					for (Register reg1 : registers) {
						if (reg1.getReg().equals(op1)) {
							String val = toBinary(Integer.toString((toInt(reg1.getVal()) - toInt(reg2.getVal()))));
							reg1.setVal(val);
							String encoded = "00011 " + reg1.getCode() + " "
									+ toBinary(Integer.toString((toInt(reg2.getVal()))));
							ins.push(input, counter, encoded, 2);
							ins.setResult(val);
							ins.setNum(toInt(val));
							ins.setReg(reg1.getReg());
						}
					}
				}
			}
		} else {
			String value = toBinary(op2);
			for (Register reg1 : registers) {
				if (reg1.getReg().equals(op1)) {
					String val = toBinary(Integer.toString((toInt(reg1.getVal()) - toInt(value))));
					reg1.setVal(val);
					String encoded = "00011 " + reg1.getCode() + " " + toBinary(Integer.toString((toInt(value))));
					ins.push(input, counter, encoded, 2);
					ins.setResult(val);
					ins.setNum(toInt(val));
					ins.setReg(reg1.getReg());
				}
			}

		}
		pc.add(ins);
	}

	public static void mul(ArrayList<Register> registers, ArrayList<PC> pc, String op1, String op2, int counter) {
		String input = "mul " + op1 + " " + op2;
		PC ins = new PC();
		if (check(registers, op2) == true) {
			for (Register reg2 : registers) {
				if (reg2.getReg().equals(op2)) {
					for (Register reg1 : registers) {
						if (reg1.getReg().equals(op1)) {
							if (toInt(reg1.getVal()) != 0 && toInt(reg2.getVal()) != 0) {
								String val = toBinaryMul(
										Integer.toString((toInt(reg1.getVal()) * toInt(reg2.getVal()))));
								reg1.setVal(val);
								String encoded = "00100 " + reg1.getCode() + " "
										+ toBinary(Integer.toString((toInt(reg2.getVal()))));
								ins.push(input, counter, encoded, 4);
								ins.setResult(val);
								ins.setNum(toInt(val));
								ins.setReg(reg1.getReg());
								ins.setRm(1);
							} else if (toInt(reg1.getVal()) == 0 || toInt(reg2.getVal()) == 0) {
								reg1.setVal("0000000000000000");
								String encoded = "00100 " + reg1.getCode() + " " + "0000000000000000";
								ins.push(input, counter, encoded, 4);
								ins.setResult("0000000000000000");
								ins.setNum(toInt("0000000000000000"));
								ins.setReg(reg1.getReg());
								ins.setRm(0);
							}
						}
					}
				}
			}
		} else {
			String value = toBinary(op2);
			for (Register reg1 : registers) {
				if (reg1.getReg().equals(op1)) {
					if (toInt(reg1.getVal()) != 0 && toInt(value) != 0) {
						String val = toBinaryMul(Integer.toString((toInt(reg1.getVal()) * toInt(value))));
						reg1.setVal(val);
						String encoded = "00100 " + reg1.getCode() + " " + toBinary(Integer.toString((toInt(value))));
						ins.push(input, counter, encoded, 4);
						ins.setResult(val);
						ins.setNum(toInt(val));
						ins.setReg(reg1.getReg());
						ins.setRm(1);
					} else if (toInt(reg1.getVal()) == 0 || toInt(value) == 0) {
						reg1.setVal("0000000000000000");
						String encoded = "00100 " + reg1.getCode() + " " + "0000000000000000";
						ins.push(input, counter, encoded, 4);
						ins.setResult("0000000000000000");
						ins.setNum(toInt("0000000000000000"));
						ins.setReg(reg1.getReg());
						ins.setRm(0);
					}
				}
			}
		}
		pc.add(ins);
	}

	public static void mov(ArrayList<Register> registers, ArrayList<PC> pc, String op1, String op2, int counter) {
		String input = "mov " + op1 + " " + op2;
		PC ins = new PC();
		if (check(registers, op2) == true) {
			for (Register reg2 : registers) {
				if (reg2.getReg().equals(op2)) {
					for (Register reg1 : registers) {
						if (reg1.getReg().equals(op1)) {
							String val = reg2.getVal();
							reg1.setVal(val);
							String encoded = "00001 " + reg1.getCode() + " " + reg2.getVal();
							ins.push(input, counter, encoded, 1);
							ins.setResult(val);
							ins.setNum(toInt(val));
							ins.setReg(reg1.getReg());
						}
					}
				}
			}
		} else {
			String value = toBinary(op2);
			for (Register reg1 : registers) {
				if (reg1.getReg().equals(op1)) {
					reg1.setVal(value);
					String encoded = "00001 " + reg1.getCode() + " " + value;
					ins.push(input, counter, encoded, 1);
					ins.setResult(value);
					ins.setNum(toInt(value));
					ins.setReg(reg1.getReg());
				}
			}
		}
		pc.add(ins);
	}

	public static void div(ArrayList<Register> registers, ArrayList<PC> pc, String op1, String op2, int counter) {
		String input = "div " + op1 + " " + op2;
		PC ins = new PC();
		if (check(registers, op2) == true) {
			for (Register reg2 : registers) {
				if (reg2.getReg().equals(op2)) {
					for (Register reg1 : registers) {
						if (reg1.getReg().equals(op1)) {
							if (toInt(reg2.getVal()) != 0) {
								String val = toBinary(Integer.toString((toInt(reg1.getVal()) / toInt(reg2.getVal()))));
								String rem = toBinary(Integer.toString((toInt(reg1.getVal()) % toInt(reg2.getVal()))));
								reg1.setVal(val);
								String encoded = "00101 " + reg1.getCode() + " "
										+ toBinary(Integer.toString((toInt(reg2.getVal()))));
								ins.push(input, counter, encoded, 4);
								ins.setResult(val);
								ins.setNum(toInt(val));
								ins.setReg(reg1.getReg());
								ins.setRe(Integer.toString(toInt(rem)) + " [" + rem + "]");
							} else {
								System.out.println("Cannot divide by zero");
								break;
							}
						}
					}
				}
			}
		} else {
			String value = toBinary(op2);
			for (Register reg1 : registers) {
				if (reg1.getReg().equals(op1)) {
					if (toInt(value) != 0) {
						String val = toBinary(Integer.toString((toInt(reg1.getVal()) / toInt(value))));
						String rem = toBinary(Integer.toString((toInt(reg1.getVal()) % toInt(value))));
						reg1.setVal(val);
						String encoded = "00101 " + reg1.getCode() + " " + toBinary(Integer.toString((toInt(value))));
						ins.push(input, counter, encoded, 4);
						ins.setResult(val);
						ins.setNum(toInt(val));
						ins.setReg(reg1.getReg());
						ins.setRe(Integer.toString(toInt(rem)) + " [" + rem + "]");
					} else {
						System.out.println("Cannot divide by zero");
						break;
					}

				}
			}
		}

		pc.add(ins);
	}
}
