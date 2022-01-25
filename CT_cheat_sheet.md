# Cortex-M Architecture

## CPU Model

<img src="resources/cpu_model.png">

* 16 Core Registers:
  * Each 32-bit wide
  * Low registers: R0-R7 (can be represented with 3 bit)
  * High registers: R8-R12 (can be represented with 4 bit)
  * SP: Stack Pointer: Last-In First-Out temporary data storage
  * LR: Link Register: Return from procedures
  * PC: Program counter: Address of next instruction
* ALU: Arithmetic Logic Unit
  * 32-bit wide (inputs A and B output is C)
* APSR (Flags)
  * Bits set based on results from ALU:
    * N = Negative, Z = Zero, C = Carry, V = Overflow
* Control Unit with IR
  * Machine code (opcode) that is currently executed
* Bus Interface

## Instruction set and programm execution
<img src="resources/instructin_set_label.png">

* The assbemlber converts each human readable Assembly instruction to a 16-bit (2byte) opcode.
  * Because of this the Memory Adress always increments by two. 

<img src="resources/instruction_set.png">

The generated Programm then loaded in to the `code area` in memory (RAM) for us the linker puts it at adress **0x0800'0000** and the `PC` loads the start adress of the programm from a specified **starting adress** for us this is **0x0000'0004** and point then to **0x0800'0000**

* Execution of a generall ARM programm.
    * Reset
    * The starting adress of the programm gets loaded over the `adress buss` from `0x0000'0004` ain to the `PC` 
    * It then loads the 2byte instruction in to the `IR` 
    * Before the execution it then increments the `PC = PC + 2`
    * Then the insturction in the Instruction Register `IR` gets executed
    * The process then repeats itself starting at loading the next instruction from the `PC`

<img src="resources/programm_execution.png">

## Memory Map
<img src="resources/memory_map.png">

* Adress space = 4GB = 2^32bits
* Ranging from *0x0000'0000* to *0xFFFF'FFFF*
* on-chip RAM:
  * SRAM1 112 Kbyte
  * SRAM2 16 Kbyte
  * SRAM3 64 Kbyte 
* system (boot)
  * Flash storage: place where the programm gets loaded (thats why the programm starts at 0x0000'0800 here the "RAM" BOOT ST ETC takes up space )
* CT Board I/O
  * status of all perpipherial devices on board like led and switches 

## Little and Big Endian
* `Little Endian` = The "least significant byte" gets stored at the lowest adress
* `Big Endian` = The "most significant byte" gets stored at the lowest adress. 
* Example of storing the value **0xA1B2'C3D4**
```
      A1       B2       C3       D4
10100001 10110010 11000011 11010100
```
<img src="resources/little_and_big_endian.png">

## Object File Sections
// todo

























