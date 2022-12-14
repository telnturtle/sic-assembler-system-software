-- SIC assembler by turtle
import System.IO
import Data.List.Split -- fn: splitOn
import Data.List -- B.isPrefixOf



instToOpcode :: String -> {-Maybe -}String
-- opcode -> hexadecimal
instToOpcode inst = case inst of 
    "ADD"   -> "18"
    "AND"   -> "40"
    "COMP"  -> "28"
    "DIV"   -> "24"
    "J"     -> "3C"
    "JEQ"   -> "30"
    "JGT"   -> "34"
    "JLT"   -> "38"
    "JSUB"  -> "48"
    "LDA"   -> "00"
    "LDCH"  -> "50"
    "LDL"   -> "08"
    "LDX"   -> "04"
    "MUL"   -> "20"
    "OR"    -> "44"
    "RD"    -> "D8"
    "RSUB"  -> "4C"
    "STA"   -> "0C"
    "STCH"  -> "54"
    "STL"   -> "14"
    "STSW"  -> "E8"
    "STX"   -> "10"
    "SUB"   -> "1C"
    "TD"    -> "E0"
    "TIX"   -> "2C"
    "WD"    -> "DC"

consPassOne :: [String] -> PassOne -> PassOne
consPassOne l1 (PassOne l2 s locctr) = PassOne ([l1] ++ l2) s locctr

hexChar :: Char -> Int
hexChar ch
    | ch == '0' = 0
    | ch == '1' = 1
    | ch == '2' = 2
    | ch == '3' = 3
    | ch == '4' = 4
    | ch == '5' = 5
    | ch == '6' = 6
    | ch == '7' = 7
    | ch == '8' = 8
    | ch == '9' = 9
    | ch == 'A' = 10
    | ch == 'B' = 11
    | ch == 'C' = 12
    | ch == 'D' = 13
    | ch == 'E' = 14
    | ch == 'F' = 15
    | ch == 'a' = 10
    | ch == 'b' = 11
    | ch == 'c' = 12
    | ch == 'd' = 13
    | ch == 'e' = 14
    | ch == 'f' = 15
    | otherwise     = 0

hexToDec :: String -> Int
hexToDec hxStr = go (reverse hxStr)
    where go []     = 0
          go (x:xs) = hexChar x + 16 * hexToDec xs

fn0 :: PassOne -> PassOne
fn0 arg@(PassOne [] _ _ ) = arg

fn0 (PassOne (l:ls) ss locctr) = 
    if ( l !! 0 ) !! 0 == '.' then fn0 (PassOne ls ss locctr) else
        if l !! 1 \= "end" then (PassOne (l:ls) ss locctr) else
            let sVal = if l !! 0 == "" then ss else ss ++ [SymType (l !! 2) ( show locctr)]
                in  case l !! 1 of 
                        "word" -> (l ++ [show locctr]) `consPassOne` fn0 ( PassOne ls sVal (locctr + 3) )
                        "resw" -> (l ++ [show locctr]) `consPassOne` fn0 ( PassOne ls sVal (locctr + 3* read (l !! 2)) )
                        "resb" -> (l ++ [show locctr]) `consPassOne` fn0 ( PassOne ls sVal (locctr + read (l !! 2)) )
                        "byte" -> (l ++ [show locctr]) `consPassOne` fn0 ( PassOne ls sVal (locctr + 3*valval) )
                            where valval = if (l !! 2) !! 1 == 'c' then read $ drop 2 $ reverse $ drop 1 $ reverse $ l !! 2 else hexToDec $ drop 2 $ reverse $ drop 1 $ reverse $ l !! 2
                        _      -> fn0 ( PassOne ls sVal (locctr + 3) )
                        -- _(inst in optab)-> add 3(instruction length) to locctr




-- pass one 
-- end ?????? ????????? ?????? ?????????
-- ??????: resw, etc. -> opcode -> error flag , ?????? ??????: opcode -> resw, etc. -> error flag
-- duplicate symbol -> ???????????? ?????? symbol ??? ????????? ???????????? ?????? (v. 0)

-- symtab??? ????????? ????????????
-- symtab??? pass one ?????? ?????? ???????????? ????????? ???
-- ????????? ????????? ??????
-- symtab??? symbolName:address ??? ????????? ??????
-- ?????? ????????? ????????? -> ????????? ??????

data SymType = SymType { name :: String , address :: String }
data PassOne = PassOne [[String]] [SymType] Int



main = do
    putStrLn "enter file name: "
    sourceFileName <- getLine
    handleS <- openFile sourceFileName ReadMode
    contentsS <- hGetContents handleS
    
    let parsedByTabs0 = map (splitOn "\t") $ splitOn "\n" contentsS
        starting_address = if head parsedByTabs0 !! 1 == "start" then
            head $ read $ head parsedByTabs0 !! 2 else 0
        afterPassOne = PassOne parsedByTabs0 [] starting_address
    
    mapM putStrLn (myListOfPassOne afterPassOne)
    putStrLn "\nhi"
    mapM putStrLn $ map strSymType (symTypeofPassOne afterPassOne)







myListOfPassOne :: PassOne -> [String]
myListOfPassOne p = map fn $ listOfPassOne p
    where
        listOfPassOne :: PassOne -> [[String]]
        listOfPassOne (PassOne list _ _) = list

        fn :: [String] -> String
        fn [] = []
        fn (s:ss) = s ++ "\t" ++ fn ss


strSymType = \(SymType name addr) -> name ++ ", " ++ addr
symTypeofPassOne (PassOne l s loc) = s