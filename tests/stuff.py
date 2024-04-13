Cell[CellGroupData[{Cell[BoxData[
    RowBox[{
        RowBox[{"angtest", "[",
                RowBox[{
                    RowBox[{"p1", ":",
                            RowBox[{"{",
                                    RowBox[{"x1_", ",", "y1_"}], "}"}]}], ",",
                    RowBox[{"p2", ":",
                            RowBox[{"{",
                                    RowBox[{"x2_", ",", "y2_"}], "}"}]}]}], "]"}], ":=",
        RowBox[{
            RowBox[{"p1", ".",
                    RowBox[{"{",
                            RowBox[{
                                RowBox[{"{",
                                        RowBox[{"0", ",",
                                                RowBox[{"-", "1"}]}], "}"}], ",",
                                RowBox[{"{",
                                        RowBox[{"1", ",", "0"}], "}"}]}], "}"}], ".", "p2"}], ">",
            "0"}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.7870624116282597` * ^ 9}, 3.7886415939165 * ^ 9},
CellLabel->"In[1]:=",
CellID->1296096117],

Cell[BoxData[
    RowBox[{
        RowBox[{"(*", " ",
                RowBox[{
                    "test", " ", "if", " ", "point", " ", "pt", " ", "is", " ",
                    "inside", " ", "convex", " ", "polygon", " ", "poly"}], " ",
                "*)"}], "\[IndentingNewLine]",
        RowBox[{
            RowBox[{
                RowBox[{"ptInPoly", "[",
                        RowBox[{"poly_", ",", "pt_"}], "]"}], ":=", "\n", "\t\t\t",
                RowBox[{"(*", " ",
                        RowBox[{
                            "translate", " ", "poly", " ", "such", " ", "that", " ", "pt",
                            " ", "becomes", " ", "the", " ", "origin"}], " ", "*)"}], "\n",
                "\t\t\t",
                RowBox[{
                    RowBox[{
                        RowBox[{
                            RowBox[{
                                RowBox[{"poly", "//",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    RowBox[{"#", "-", "pt"}], "&"}], "/@", "#"}], "&"}]}], "//",
                                "\n", "\t\t\t",
                                RowBox[{"(*", " ",
                                        RowBox[{
                                            "pt", " ", "is", " ", "inside", " ", "if", " ", "adjacent",
                                            " ", "vertex", " ", "vector", " ", "pair", " ", "angles",
                                            " ", "are", " ", "all", " ", "positive", " ", "or", " ",
                                            "all", " ", "negative"}], " ", "*)"}], "\n", "\t\t\t",
                                RowBox[{
                                    RowBox[{"{",
                                            RowBox[{"#", ",",
                                                    RowBox[{"RotateLeft", "@", "#"}]}], "}"}], "&"}]}], "//",
                            "Transpose"}], "//",
                        RowBox[{
                            RowBox[{
                                RowBox[{
                                    RowBox[{"angtest", "@@", "#"}], "&"}], "/@", "#"}], "&"}]}],
                    "//",
                    RowBox[{
                        RowBox[{"Equal", "@@", "#"}], "&"}]}]}], "\[IndentingNewLine]",

            RowBox[{
                RowBox[{"ptInPolys", "[",
                        RowBox[{"polys_", ",", "pt_"}], "]"}], ":=",
                RowBox[{"Or", "@@",
                        RowBox[{"(",
                                RowBox[{
                                    RowBox[{
                                        RowBox[{"ptInPoly", "[",
                                                RowBox[{"#", ",", "pt"}], "]"}], "&"}], "/@", "polys"}],
                                ")"}], " "}]}]}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.787062434393622 * ^ 9}, {3.7870625047488813
` * ^ 9,
3.787062505364286 * ^ 9}, 3.78864159391656 * ^ 9},
CellLabel->"In[2]:=",
CellID->1833180722],

Cell[BoxData[
    RowBox[{
        RowBox[{"(*",
                RowBox[{
                    "Is", " ", "point", " ", "pt", " ", "inside", " ", "list", " ",
                    "of", " ", "polygons", " ",
                    RowBox[{"polys", "?"}]}], "*)"}], "\[IndentingNewLine]",
        RowBox[{
            RowBox[{"pathOK", "[",
                    RowBox[{"ps_", ",", "pe_", ",", "polys_", ",", "delta_"}], "]"}],
            ":=",
            RowBox[{"Module", "[",
                    RowBox[{
                        RowBox[{"{",
                                RowBox[{"dist", ",", "n", ",", "pt"}], "}"}], ",",
                        "\[IndentingNewLine]",
                        RowBox[{
                            RowBox[{"dist", " ", "=", " ",
                                    RowBox[{"Norm", "[",
                                            RowBox[{"ps", "-", "pe"}], "]"}]}], ";", " ",
                            RowBox[{"(*",
                                    RowBox[{
                                        "Primitive", " ", "collision", " ", "checking", " ", "that",
                                        " ", "checks", " ", "every", " ", "delta", " ", "distance",
                                        " ", "along", " ", "a", " ", "line", " ", "from", " ", "ps",
                                        " ", "to", " ", "pe", " ", "for", " ", "collisions", " ",
                                        "with", " ",
                                        RowBox[{"polygons", "."}]}], " ", "*)"}],
                            "\[IndentingNewLine]",
                            RowBox[{"If", "[",
                                    RowBox[{
                                        RowBox[{"dist", "\[LessEqual]", " ", "delta"}], ",",
                                        "\[IndentingNewLine]", "True", ",", "\[IndentingNewLine]",
                                        RowBox[{
                                            RowBox[{"n", "=",
                                                    RowBox[{"Ceiling", "[",
                                                            RowBox[{"dist", "/", "delta"}], "]"}]}], ";",
                                            "\[IndentingNewLine]",
                                            RowBox[{"!",
                                                    RowBox[{"Or", "@@",
                                                            RowBox[{"Table", "[",
                                                                    RowBox[{
                                                                        RowBox[{
                                                                            RowBox[{"pt", " ", "=", " ",
                                                                                    RowBox[{"ps", "+", " ",
                                                                                            RowBox[{
                                                                                                RowBox[{"(",
                                                                                                        RowBox[
                                                                                                            {"pe", "-",
                                                                                                             "ps"}],
                                                                                                        ")"}], "*",
                                                                                                FractionBox["i",
                                                                                                RowBox[{"n", "+",
                                                                                                        "1"}]]}]}]}],
                                                                            ";",
                                                                            "\[IndentingNewLine]",
                                                                            RowBox[{"ptInPolys", "[",
                                                                                    RowBox[{"polys", ",", "pt"}],
                                                                                    "]"}]}], ",",
                                                                        RowBox[{"{",
                                                                                RowBox[{"i", ",", "1", ",", "n"}],
                                                                                "}"}]}],
                                                                    "]"}]}]}]}]}], "]"}]}]}], "\[IndentingNewLine]",
                    "]"}]}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.787062441512422 * ^ 9}, 3.7870625481585407
` * ^ 9,
3.787062845199584 * ^ 9, 3.788641593916608 * ^ 9},
CellLabel->"In[4]:=",
CellID->190124536],

Cell[BoxData[
    RowBox[{
        RowBox[{"pathOKT", "[",
                RowBox[{"ps_", ",", "pe_", ",", "polys_", ",", "delta_"}], "]"}], ":=",
        RowBox[{"Module", "[",
                RowBox[{
                    RowBox[{"{",
                            RowBox[{
                                "dist", ",", "n", ",", "pt", ",", "dx", ",", "dx2", ",", "dy",
                                ",", "dy2"}], "}"}], ",", "\[IndentingNewLine]",
                    RowBox[{"(*",
                            RowBox[{
                                RowBox[{
                                    "Primitive", " ", "collision", " ", "checking", " ", "that",
                                    " ", "checks", " ", "every", " ", "delta", " ", "distance",
                                    " ", "along", " ", "a", " ", "line", " ", "from", " ", "ps",
                                    " ", "to", " ", "pe", " ", "for", " ", "collisions", " ",
                                    "with", " ", "polygons"}], ",", " ",
                                RowBox[{"uses", " ", "toriod", " ",
                                        RowBox[{"assumption", "."}]}]}], " ", "*)"}],
                    "\[IndentingNewLine]",
                    RowBox[{"(*",
                            RowBox[{"toroid", " ", "assumption"}], "*)"}],
                    "\[IndentingNewLine]",
                    RowBox[{
                        RowBox[{"dx", " ", "=", " ",
                                RowBox[{"Abs", "[",
                                        RowBox[{
                                            RowBox[{
                                                "pe", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                            "-",
                                            RowBox[{
                                                "ps", "\[LeftDoubleBracket]", "1",
                                                "\[RightDoubleBracket]"}]}], "]"}]}], ";",
                        "\[IndentingNewLine]",
                        RowBox[{"dx2", " ", "=",
                                RowBox[{
                                    RowBox[{"2", "\[Pi]"}], "-", " ", "dx"}]}], ";",
                        "\[IndentingNewLine]",
                        RowBox[{"dy", " ", "=", " ",
                                RowBox[{"Abs", "[",
                                        RowBox[{
                                            RowBox[{
                                                "pe", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                            "-",
                                            RowBox[{
                                                "ps", "\[LeftDoubleBracket]", "2",
                                                "\[RightDoubleBracket]"}]}], "]"}]}], ";",
                        "\[IndentingNewLine]",
                        RowBox[{"dy2", " ", "=",
                                RowBox[{
                                    RowBox[{"2", "\[Pi]"}], "-", "dy"}]}], " ", ";", " ",
                        "\[IndentingNewLine]", "\[IndentingNewLine]",
                        RowBox[{"dx", "=",
                                RowBox[{
                                    RowBox[{
                                        "pe", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                    "-",
                                    RowBox[{
                                        "ps", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                    "+",
                                    RowBox[{"If", "[",
                                            RowBox[{
                                                RowBox[{"dx", "<", "dx2"}], ",", "0", ",", " ",
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{
                                                                RowBox[{
                                                                    "pe", "\[LeftDoubleBracket]", "1",
                                                                    "\[RightDoubleBracket]"}], ">",
                                                                RowBox[{
                                                                    "ps", "\[LeftDoubleBracket]", "1",
                                                                    "\[RightDoubleBracket]"}]}], ",",
                                                            RowBox[{
                                                                RowBox[{"-", "2"}], "\[Pi]"}], ",",
                                                            RowBox[{
                                                                RowBox[{"+", "2"}], "\[Pi]"}]}], "]"}]}], "]"}]}]}],
                        ";",
                        "\[IndentingNewLine]",
                        RowBox[{"dy", "=",
                                RowBox[{
                                    RowBox[{
                                        "pe", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                    "-",
                                    RowBox[{
                                        "ps", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                    "+",
                                    RowBox[{"If", "[",
                                            RowBox[{
                                                RowBox[{"dy", "<", "dy2"}], ",", "0", ",", " ",
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{
                                                                RowBox[{
                                                                    "pe", "\[LeftDoubleBracket]", "2",
                                                                    "\[RightDoubleBracket]"}], ">",
                                                                RowBox[{
                                                                    "ps", "\[LeftDoubleBracket]", "2",
                                                                    "\[RightDoubleBracket]"}]}], ",",
                                                            RowBox[{
                                                                RowBox[{"-", "2"}], "\[Pi]"}], ",",
                                                            RowBox[{
                                                                RowBox[{"+", "2"}], "\[Pi]"}]}], "]"}]}], "]"}]}]}],
                        ";",
                        "\[IndentingNewLine]", "\[IndentingNewLine]",
                        RowBox[{"dist", " ", "=", " ",
                                SqrtBox[
                                    RowBox[{
                                        SuperscriptBox["dx", "2"], "+",
                                        SuperscriptBox["dy", "2"]}]]}], ";", "\[IndentingNewLine]",
                        RowBox[{"If", "[",
                                RowBox[{
                                    RowBox[{"dist", "\[LessEqual]", " ", "delta"}], ",",
                                    "\[IndentingNewLine]", "True", ",", "\[IndentingNewLine]",
                                    RowBox[{
                                        RowBox[{"n", "=",
                                                RowBox[{"Ceiling", "[",
                                                        RowBox[{"dist", "/", "delta"}], "]"}]}], ";",
                                        "\[IndentingNewLine]",
                                        RowBox[{"!",
                                                RowBox[{"Or", "@@",
                                                        RowBox[{"Table", "[",
                                                                RowBox[{
                                                                    RowBox[{
                                                                        RowBox[{"pt", " ", "=", " ",
                                                                                RowBox[{"ps", "+", " ",
                                                                                        RowBox[{
                                                                                            RowBox[{"{",
                                                                                                    RowBox[{"dx", ",",
                                                                                                            "dy"}],
                                                                                                    "}"}], "*",
                                                                                            FractionBox["i",
                                                                                            RowBox[
                                                                                                {"n", "+", "1"}]]}]}]}],
                                                                        ";",
                                                                        "\[IndentingNewLine]",
                                                                        RowBox[{"If", "[",
                                                                                RowBox[{
                                                                                    RowBox[{
                                                                                        RowBox[{
                                                                                            "pt",
                                                                                            "\[LeftDoubleBracket]", "1",
                                                                                            "\[RightDoubleBracket]"}],
                                                                                        "<", "0"}], ",",
                                                                                    RowBox[{
                                                                                        RowBox[{
                                                                                            "pt",
                                                                                            "\[LeftDoubleBracket]", "1",
                                                                                            "\[RightDoubleBracket]"}],
                                                                                        "=",
                                                                                        RowBox[{
                                                                                            RowBox[{
                                                                                                "pt",
                                                                                                "\[LeftDoubleBracket]",
                                                                                                "1",
                                                                                                "\[RightDoubleBracket]"}],
                                                                                            "+",
                                                                                            RowBox[
                                                                                                {"2", "\[Pi]"}]}]}]}],
                                                                                "]"}], ";",
                                                                        "\[IndentingNewLine]",
                                                                        RowBox[{"If", "[",
                                                                                RowBox[{
                                                                                    RowBox[{
                                                                                        RowBox[{
                                                                                            "pt",
                                                                                            "\[LeftDoubleBracket]", "1",
                                                                                            "\[RightDoubleBracket]"}],
                                                                                        ">",
                                                                                        RowBox[{"2", "\[Pi]"}]}], ",",
                                                                                    RowBox[{
                                                                                        RowBox[{
                                                                                            "pt",
                                                                                            "\[LeftDoubleBracket]", "1",
                                                                                            "\[RightDoubleBracket]"}],
                                                                                        "=",
                                                                                        RowBox[{
                                                                                            RowBox[{
                                                                                                "pt",
                                                                                                "\[LeftDoubleBracket]",
                                                                                                "1",
                                                                                                "\[RightDoubleBracket]"}],
                                                                                            "-",
                                                                                            RowBox[
                                                                                                {"2", "\[Pi]"}]}]}]}],
                                                                                "]"}], ";",
                                                                        "\[IndentingNewLine]",
                                                                        RowBox[{"If", "[",
                                                                                RowBox[{
                                                                                    RowBox[{
                                                                                        RowBox[{
                                                                                            "pt",
                                                                                            "\[LeftDoubleBracket]", "2",
                                                                                            "\[RightDoubleBracket]"}],
                                                                                        "<", "0"}], ",",
                                                                                    RowBox[{
                                                                                        RowBox[{
                                                                                            "pt",
                                                                                            "\[LeftDoubleBracket]", "2",
                                                                                            "\[RightDoubleBracket]"}],
                                                                                        "=",
                                                                                        RowBox[{
                                                                                            RowBox[{
                                                                                                "pt",
                                                                                                "\[LeftDoubleBracket]",
                                                                                                "2",
                                                                                                "\[RightDoubleBracket]"}],
                                                                                            "+",
                                                                                            RowBox[
                                                                                                {"2", "\[Pi]"}]}]}]}],
                                                                                "]"}], ";",
                                                                        "\[IndentingNewLine]",
                                                                        RowBox[{"If", "[",
                                                                                RowBox[{
                                                                                    RowBox[{
                                                                                        RowBox[{
                                                                                            "pt",
                                                                                            "\[LeftDoubleBracket]", "2",
                                                                                            "\[RightDoubleBracket]"}],
                                                                                        ">",
                                                                                        RowBox[{"2", "\[Pi]"}]}], ",",
                                                                                    RowBox[{
                                                                                        RowBox[{
                                                                                            "pt",
                                                                                            "\[LeftDoubleBracket]", "2",
                                                                                            "\[RightDoubleBracket]"}],
                                                                                        "=",
                                                                                        RowBox[{
                                                                                            RowBox[{
                                                                                                "pt",
                                                                                                "\[LeftDoubleBracket]",
                                                                                                "2",
                                                                                                "\[RightDoubleBracket]"}],
                                                                                            "-",
                                                                                            RowBox[
                                                                                                {"2", "\[Pi]"}]}]}]}],
                                                                                "]"}], ";",
                                                                        "\[IndentingNewLine]",
                                                                        RowBox[{"ptInPolys", "[",
                                                                                RowBox[{"polys", ",", "pt"}], "]"}]}],
                                                                    ",",
                                                                    RowBox[{"{",
                                                                            RowBox[{"i", ",", "1", ",", "n"}], "}"}]}],
                                                                "]"}]}]}]}]}], "]"}]}]}], "\[IndentingNewLine]",
                "]"}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.787062448331089 * ^ 9}, {3.7870625675984993
` * ^ 9,
3.787062577666945 * ^ 9}, 3.787062846436304 * ^ 9,
3.7886415939166517
` * ^ 9},
CellLabel->"In[5]:=",
CellID->604433311],

Cell[BoxData[
    RowBox[{"toroidDist", " ", ":=",
            RowBox[{"(*", " ",
                    RowBox[{
                        RowBox[{"Toroid", " ", "assumption"}], ",", " ",
                        RowBox[{
                            "wraps", " ", "from", " ", "2", "\[Pi]", " ", "to", " ", "0."}]}],
                    " ", "*)"}], " ",
            RowBox[{"(",
                    RowBox[{
                        RowBox[{"\[Sqrt]",
                                RowBox[{"(",
                                        RowBox[{
                                            RowBox[{"Min", "[",
                                                    RowBox[{
                                                        SuperscriptBox[
                                                            RowBox[{"(",
                                                                    RowBox[{
                                                                        RowBox[{
                                                                            "#1", "\[LeftDoubleBracket]", "1",
                                                                            "\[RightDoubleBracket]"}], "-",
                                                                        RowBox[{
                                                                            "#2", "\[LeftDoubleBracket]", "1",
                                                                            "\[RightDoubleBracket]"}]}], ")"}], "2"],
                                                        ",",
                                                        SuperscriptBox[
                                                            RowBox[{"(",
                                                                    RowBox[{
                                                                        RowBox[{"2", "\[Pi]"}], "-",
                                                                        RowBox[{"Abs", "[",
                                                                                RowBox[{
                                                                                    RowBox[{
                                                                                        "#1", "\[LeftDoubleBracket]",
                                                                                        "1",
                                                                                        "\[RightDoubleBracket]"}], "-",
                                                                                    RowBox[{
                                                                                        "#2", "\[LeftDoubleBracket]",
                                                                                        "1",
                                                                                        "\[RightDoubleBracket]"}]}],
                                                                                "]"}]}], ")"}], "2"]}],
                                                    "]"}], "+",
                                            RowBox[{"Min", "[",
                                                    RowBox[{
                                                        SuperscriptBox[
                                                            RowBox[{"(",
                                                                    RowBox[{
                                                                        RowBox[{
                                                                            "#1", "\[LeftDoubleBracket]", "2",
                                                                            "\[RightDoubleBracket]"}], "-",
                                                                        RowBox[{
                                                                            "#2", "\[LeftDoubleBracket]", "2",
                                                                            "\[RightDoubleBracket]"}]}], ")"}], "2"],
                                                        ",",
                                                        SuperscriptBox[
                                                            RowBox[{"(",
                                                                    RowBox[{
                                                                        RowBox[{"2", "\[Pi]"}], "-",
                                                                        RowBox[{"Abs", "[",
                                                                                RowBox[{
                                                                                    RowBox[{
                                                                                        "#1", "\[LeftDoubleBracket]",
                                                                                        "2",
                                                                                        "\[RightDoubleBracket]"}], "-",
                                                                                    RowBox[{
                                                                                        "#2", "\[LeftDoubleBracket]",
                                                                                        "2",
                                                                                        "\[RightDoubleBracket]"}]}],
                                                                                "]"}]}], ")"}], "2"]}],
                                                    "]"}]}], " ", ")"}]}], "&"}], ")"}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.787062452818902 * ^ 9}, 3.787062591492569 * ^ 9,
3.7886415939166937
` * ^ 9},
CellLabel->"In[6]:=",
CellID->1510895881],

Cell[BoxData[
    RowBox[{
        RowBox[{"myAstar", "[",
                RowBox[{"adjL_", ",", "verts_", ",", "si_", ",", "fi_"}], "]"}], ":=",
        RowBox[{"Module", "[",
                RowBox[{
                    RowBox[{"{",
                            RowBox[{
                                "openSet", ",", "cameFrom", ",", "gScore", ",", "fScore", ",",
                                "current", ",", "currentfscore", ",", "path", ",",
                                "tentativegScore"}], "}"}], ",", "\[IndentingNewLine]",
                    RowBox[{"(*",
                            RowBox[{
                                RowBox[{
                                    RowBox[{"Computes", " ", "A"}], "-",
                                    RowBox[{
                                        "star", " ", "shortest", " ", "path", " ", "from", " ",
                                        "start", " ", "node", " ", "si", " ", "to", " ", "final", " ",
                                        "node", " ",
                                        RowBox[{"fi", ".", " ", "The"}], " ", "set", " ", "of", " ",
                                        "discovered", " ", "nodes", " ", "that", " ", "may", " ",
                                        "need", " ", "to", " ", "be", " ",
                                        RowBox[{"(",
                                                RowBox[{"re", "-"}], ")"}],
                                        RowBox[{
                                            "expanded", ".", "\[IndentingNewLine]", "Initially"}]}]}],
                                ",", " ",
                                RowBox[{
                                    "only", " ", "the", " ", "start", " ", "node", " ", "is", " ",
                                    RowBox[{"known", "."}]}]}], "*)"}], "\[IndentingNewLine]",
                    RowBox[{
                        RowBox[{"openSet", "=",
                                RowBox[{"{", "si", "}"}]}], ";", "\[IndentingNewLine]",
                        RowBox[{"cameFrom", "=", " ",
                                RowBox[{"ConstantArray", "[",
                                        RowBox[{
                                            RowBox[{"-", "1"}], ",", " ",
                                            RowBox[{"Length", "[", "verts", "]"}]}], "]"}]}], ";", " ",
                        "\[IndentingNewLine]",
                        RowBox[{"(*",
                                RowBox[{
                                    RowBox[{"For", " ", "node", " ", "n"}], ",", " ",
                                    RowBox[{
                                        RowBox[{"cameFrom", "[", "n", "]"}], " ", "is", " ", "the",
                                        " ", "node", " ", "immediately", " ", "preceding", " ", "it",
                                        " ", "on", " ", "the", " ", "cheapest", " ", "path", " ",
                                        "from", " ", "start", " ", "to", " ", "n", " ", "currently",
                                        " ",
                                        RowBox[{"known", "."}]}]}], "*)"}], "\[IndentingNewLine]",
                        RowBox[{"gScore", " ", "=", " ",
                                RowBox[{"ConstantArray", "[",
                                        RowBox[{"\[Infinity]", ",", " ",
                                                RowBox[{"Length", "[", "verts", "]"}]}], "]"}]}], ";", " ",
                        RowBox[{"(*",
                                RowBox[{
                                    RowBox[{"For", " ", "node", " ", "n"}], ",",
                                    RowBox[{
                                        RowBox[{"gScore", "[", "n", "]"}], " ", "is", " ", "the", " ",
                                        "cost", " ", "of", " ", "the", " ", "cheapest", " ", "path",
                                        " ", "from", " ", "start", " ", "to", " ", "n", " ",
                                        "currently", " ",
                                        RowBox[{"known", "."}]}]}], "*)"}], "\[IndentingNewLine]",
                        RowBox[{
                            RowBox[{
                                "gScore", "\[LeftDoubleBracket]", "si",
                                "\[RightDoubleBracket]"}], " ", "=", " ", "0"}], ";",
                        "\[IndentingNewLine]",
                        RowBox[{"(*",
                                RowBox[{
                                    RowBox[{"For", " ", "node", " ", "n"}], ",", " ",
                                    RowBox[{
                                        RowBox[{"fScore", "[", "n", "]"}], ":=",
                                        RowBox[{
                                            RowBox[{"gScore", "[", "n", "]"}], "+",
                                            RowBox[{"h",
                                                    RowBox[{
                                                        RowBox[{"(", "n", ")"}], "."}]}]}]}]}], "*)"}],
                        "\[IndentingNewLine]",
                        RowBox[{"fScore", "=", " ",
                                RowBox[{"ConstantArray", "[",
                                        RowBox[{"\[Infinity]", ",", " ",
                                                RowBox[{"Length", "[", "verts", "]"}]}], "]"}]}], ";", " ",
                        RowBox[{"(*",
                                RowBox[{
                                    "Map", " ", "with", " ", "default", " ", "value", " ", "of",
                                    " ",
                                    RowBox[{"infinity", "."}]}], "*)"}], "\[IndentingNewLine]",
                        RowBox[{
                            RowBox[{
                                "fScore", "\[LeftDoubleBracket]", "si",
                                "\[RightDoubleBracket]"}], "=",
                            RowBox[{"toroidDist", "[",
                                    RowBox[{
                                        RowBox[{
                                            "verts", "\[LeftDoubleBracket]", "si",
                                            "\[RightDoubleBracket]"}], " ", ",", " ",
                                        RowBox[{
                                            "verts", "\[LeftDoubleBracket]", "fi",
                                            "\[RightDoubleBracket]"}]}], "]"}]}], ";",
                        "\[IndentingNewLine]",
                        RowBox[{"While", "[",
                                RowBox[{
                                    RowBox[{
                                        RowBox[{"Length", "[", "openSet", "]"}], ">", "0"}], " ",
                                    RowBox[{"(*",
                                            RowBox[{"&&", " ",
                                                    RowBox[{"ctr", "<", "10"}]}], "*)"}], ",",
                                    "\[IndentingNewLine]",
                                    RowBox[{"(*",
                                            RowBox[{"current", ":=",
                                                    RowBox[{
                                                        "the", " ", "node", " ", "in", " ", "openSet", " ", "having",
                                                        " ", "the", " ", "lowest", " ",
                                                        RowBox[{"fScore", "[", "]"}], " ", "value"}]}], "*)"}],
                                    "\[IndentingNewLine]",
                                    RowBox[{
                                        RowBox[{"currentfscore", " ", "=", " ",
                                                RowBox[{"Min", "[",
                                                        RowBox[{
                                                            "fScore", "\[LeftDoubleBracket]", "openSet",
                                                            "\[RightDoubleBracket]"}], "]"}]}], ";",
                                        "\[IndentingNewLine]",
                                        RowBox[{"current", " ", "=",
                                                RowBox[{"openSet", "\[LeftDoubleBracket]", " ",
                                                        RowBox[{"First", "@@",
                                                                RowBox[{"Position", "[",
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                "fScore", "\[LeftDoubleBracket]",
                                                                                "openSet",
                                                                                "\[RightDoubleBracket]"}], ",",
                                                                            "currentfscore"}],
                                                                        "]"}]}], "\[RightDoubleBracket]"}]}], ";",
                                        "\[IndentingNewLine]", "\[IndentingNewLine]",
                                        RowBox[{"If", "[", " ",
                                                RowBox[{
                                                    RowBox[{"current", " ", "\[Equal]", " ", "fi"}], ",",
                                                    "\[IndentingNewLine]",
                                                    RowBox[{
                                                        RowBox[{"path", " ", "=", " ",
                                                                RowBox[{"{", "fi", "}"}]}], ";",
                                                        RowBox[{"While", "[",
                                                                RowBox[{
                                                                    RowBox[{
                                                                        RowBox[{"First", "@", "path"}], "\[NotEqual]",
                                                                        "si"}],
                                                                    ",",
                                                                    RowBox[{"PrependTo", "[",
                                                                            RowBox[{"path", ",",
                                                                                    RowBox[{"cameFrom",
                                                                                            "\[LeftDoubleBracket]",
                                                                                            RowBox[
                                                                                                {"First", "@", "path"}],
                                                                                            "\[RightDoubleBracket]"}]}],
                                                                            "]"}]}], "]"}], ";",
                                                        "\[IndentingNewLine]",
                                                        RowBox[{"Return", "[", "path", "]"}]}]}],
                                                "\[IndentingNewLine]", "]"}], ";", "\[IndentingNewLine]",
                                        RowBox[{"openSet", " ", "=", " ",
                                                RowBox[{"DeleteCases", "[",
                                                        RowBox[{"openSet", ",", "current"}], "]"}]}], ";",
                                        "\[IndentingNewLine]",
                                        RowBox[{"Table", "[", "\[IndentingNewLine]",
                                                RowBox[{
                                                    RowBox[{
                                                        RowBox[{"tentativegScore", " ", "=", " ",
                                                                RowBox[{
                                                                    RowBox[{
                                                                        "gScore", "\[LeftDoubleBracket]", "current",
                                                                        "\[RightDoubleBracket]"}], "+",
                                                                    RowBox[{"toroidDist", "[",
                                                                            RowBox[{
                                                                                RowBox[{
                                                                                    "verts", "\[LeftDoubleBracket]",
                                                                                    "current",
                                                                                    "\[RightDoubleBracket]"}], ",",
                                                                                RowBox[{
                                                                                    "verts", "\[LeftDoubleBracket]",
                                                                                    "nbr",
                                                                                    "\[RightDoubleBracket]"}]}],
                                                                            "]"}]}]}], ";",
                                                        "\[IndentingNewLine]",
                                                        RowBox[{"If", "[",
                                                                RowBox[{
                                                                    RowBox[{"tentativegScore", "<", " ",
                                                                            RowBox[{
                                                                                "gScore", "\[LeftDoubleBracket]", "nbr",
                                                                                "\[RightDoubleBracket]"}]}], ",", "\n",
                                                                    "                ",
                                                                    RowBox[{"(*",
                                                                            RowBox[{
                                                                                "This", " ", "path", " ", "to", " ",
                                                                                "neighbor", " ",
                                                                                "is", " ", "better", " ", "than", " ",
                                                                                "any", " ",
                                                                                "previous", " ",
                                                                                RowBox[{"one", ".", " ", "Record"}],
                                                                                " ",
                                                                                RowBox[{"it", "!"}]}], "*)"}],
                                                                    "\[IndentingNewLine]",
                                                                    RowBox[{
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                "cameFrom", "\[LeftDoubleBracket]",
                                                                                "nbr",
                                                                                "\[RightDoubleBracket]"}], "=",
                                                                            "current"}], ";",
                                                                        "\[IndentingNewLine]",
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                "gScore", "\[LeftDoubleBracket]", "nbr",
                                                                                "\[RightDoubleBracket]"}], "=",
                                                                            "tentativegScore"}],
                                                                        ";",
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                "fScore", "\[LeftDoubleBracket]", "nbr",
                                                                                "\[RightDoubleBracket]"}], "=",
                                                                            RowBox[{
                                                                                RowBox[{
                                                                                    "gScore", "\[LeftDoubleBracket]",
                                                                                    "nbr",
                                                                                    "\[RightDoubleBracket]"}], "+",
                                                                                RowBox[{"toroidDist", "[",
                                                                                        RowBox[{
                                                                                            RowBox[{
                                                                                                "verts",
                                                                                                "\[LeftDoubleBracket]",
                                                                                                "nbr",
                                                                                                "\[RightDoubleBracket]"}],
                                                                                            " ", ",", " ",
                                                                                            RowBox[{
                                                                                                "verts",
                                                                                                "\[LeftDoubleBracket]",
                                                                                                "nbr",
                                                                                                "\[RightDoubleBracket]"}]}],
                                                                                        "]"}]}]}], ";",
                                                                        "\[IndentingNewLine]",
                                                                        RowBox[{"If", "[", " ",
                                                                                RowBox[{
                                                                                    RowBox[{"FreeQ", "[",
                                                                                            RowBox[{"openSet", ",",
                                                                                                    "nbr"}], "]"}], ",",
                                                                                    RowBox[{"AppendTo", "[",
                                                                                            RowBox[{"openSet", ",",
                                                                                                    "nbr"}], "]"}]}],
                                                                                "]"}]}]}],
                                                                "]"}], ";"}], "\[IndentingNewLine]", ",",
                                                    RowBox[{"{",
                                                            RowBox[{"nbr", ",",
                                                                    RowBox[{
                                                                        "adjL", "\[LeftDoubleBracket]", "current",
                                                                        "\[RightDoubleBracket]"}]}], "}"}]}], "]"}],
                                        ";"}]}],
                                "\[IndentingNewLine]", "]"}], ";", "\t", "\[IndentingNewLine]",

                        RowBox[{"Return", "[",
                                RowBox[{"-", "1"}], "]"}]}]}], " ",
                RowBox[{"(*", "Failure", "*)"}], "\[IndentingNewLine]",
                "]"}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.787062461447361 * ^ 9}, {3.787062605712956 * ^ 9,
                                             3.787062662366682 * ^ 9}, {3.78706285674129 * ^ 9,
                                                                        3.787062861578515 * ^ 9},
3.788641593916737 * ^ 9},
CellLabel->"In[7]:=",
CellID->2074799017],

Cell[BoxData[
    RowBox[{
        RowBox[{"toroidLines", "[",
                RowBox[{"pts_", ",",
                        RowBox[{"color1_:", "Blue"}], ",",
                        RowBox[{"color2_:", "-", "1"}]}], "]"}], ":=",
        "\[IndentingNewLine]",
        RowBox[{"Table", "[",
                RowBox[{
                    RowBox[{"toroidLine", "[",
                            RowBox[{"e", ",", "color1", ",", "color2"}], "]"}], ",", " ",
                    RowBox[{"{",
                            RowBox[{"e", ",", "pts"}], "}"}]}], "]"}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.787062466036467 * ^ 9}, 3.78864159391678 * ^ 9},
CellLabel->"In[8]:=",
CellID->1568142428],

Cell[BoxData[
    RowBox[{
        RowBox[{"toroidLine", "[",
                RowBox[{"e_", ",",
                        RowBox[{"color1_:", "Blue"}], ",",
                        RowBox[{"color2_:", "-", "1"}]}], "]"}], ":=",
        RowBox[{"Module", "[",
                RowBox[{
                    RowBox[{"{",
                            RowBox[{"dx", ",", "dx2", ",", "dy", ",", "dy2"}], "}"}], ",",
                    "\[IndentingNewLine]",
                    RowBox[{
                        RowBox[{"dx", " ", "=", " ",
                                RowBox[{"Abs", "[",
                                        RowBox[{
                                            RowBox[{"e", "\[LeftDoubleBracket]",
                                                    RowBox[{"2", ",", "1"}], "\[RightDoubleBracket]"}], "-",
                                            RowBox[{"e", "\[LeftDoubleBracket]",
                                                    RowBox[{"1", ",", "1"}], "\[RightDoubleBracket]"}]}],
                                        "]"}]}], ";", "\[IndentingNewLine]",
                        RowBox[{"dx2", " ", "=",
                                RowBox[{
                                    RowBox[{"2", "\[Pi]"}], "-", " ", "dx"}]}], ";",
                        "\[IndentingNewLine]",
                        RowBox[{"dy", " ", "=", " ",
                                RowBox[{"Abs", "[",
                                        RowBox[{
                                            RowBox[{"e", "\[LeftDoubleBracket]",
                                                    RowBox[{"2", ",", "2"}], "\[RightDoubleBracket]"}], "-",
                                            RowBox[{"e", "\[LeftDoubleBracket]",
                                                    RowBox[{"1", ",", "2"}], "\[RightDoubleBracket]"}]}],
                                        "]"}]}], ";", "\[IndentingNewLine]",
                        RowBox[{"dy2", " ", "=",
                                RowBox[{
                                    RowBox[{"2", "\[Pi]"}], "-", " ", "dy"}]}], " ", ";",
                        "\[IndentingNewLine]",
                        RowBox[{"If", "[",
                                RowBox[{
                                    RowBox[{
                                        RowBox[{"dx", ">", "dx2"}], " ", "||", " ",
                                        RowBox[{"dy", ">", "dy2"}]}], ",", "\[IndentingNewLine]",
                                    RowBox[{
                                        RowBox[{"dx", " ", "=",
                                                RowBox[{
                                                    RowBox[{"e", "\[LeftDoubleBracket]",
                                                            RowBox[{"2", ",", "1"}], "\[RightDoubleBracket]"}], "-",
                                                    RowBox[{"e", "\[LeftDoubleBracket]",
                                                            RowBox[{"1", ",", "1"}], "\[RightDoubleBracket]"}], "+",
                                                    RowBox[{"If", "[",
                                                            RowBox[{
                                                                RowBox[{"dx", "<", "dx2"}], ",", "0", ",", " ",
                                                                RowBox[{"If", "[",
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                RowBox[{"e", "\[LeftDoubleBracket]",
                                                                                        RowBox[{"2", ",", "1"}],
                                                                                        "\[RightDoubleBracket]"}],
                                                                                ">",
                                                                                RowBox[{"e", "\[LeftDoubleBracket]",
                                                                                        RowBox[{"1", ",", "1"}],
                                                                                        "\[RightDoubleBracket]"}]}],
                                                                            ",",
                                                                            RowBox[{
                                                                                RowBox[{"-", "2"}], "\[Pi]"}], ",",
                                                                            RowBox[{
                                                                                RowBox[{"+", "2"}], "\[Pi]"}]}],
                                                                        "]"}]}], "]"}]}]}],
                                        ";", "\[IndentingNewLine]",
                                        RowBox[{"dy", " ", "=",
                                                RowBox[{
                                                    RowBox[{"e", "\[LeftDoubleBracket]",
                                                            RowBox[{"2", ",", "2"}], "\[RightDoubleBracket]"}], "-",
                                                    RowBox[{"e", "\[LeftDoubleBracket]",
                                                            RowBox[{"1", ",", "2"}], "\[RightDoubleBracket]"}], "+",
                                                    RowBox[{"If", "[",
                                                            RowBox[{
                                                                RowBox[{"dy", "<", "dy2"}], ",", "0", ",", " ",
                                                                RowBox[{"If", "[",
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                RowBox[{"e", "\[LeftDoubleBracket]",
                                                                                        RowBox[{"2", ",", "2"}],
                                                                                        "\[RightDoubleBracket]"}],
                                                                                ">",
                                                                                RowBox[{"e", "\[LeftDoubleBracket]",
                                                                                        RowBox[{"1", ",", "2"}],
                                                                                        "\[RightDoubleBracket]"}]}],
                                                                            ",",
                                                                            RowBox[{
                                                                                RowBox[{"-", "2"}], "\[Pi]"}], ",",
                                                                            RowBox[{
                                                                                RowBox[{"+", "2"}], "\[Pi]"}]}],
                                                                        "]"}]}], "]"}]}]}],
                                        ";", " ",
                                        RowBox[{"{",
                                                RowBox[{"color1", ",",
                                                        RowBox[{"Line", "[",
                                                                RowBox[{"{",
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                "e", "\[LeftDoubleBracket]", "1",
                                                                                "\[RightDoubleBracket]"}], ",",
                                                                            RowBox[{
                                                                                RowBox[{
                                                                                    "e", "\[LeftDoubleBracket]", "1",
                                                                                    "\[RightDoubleBracket]"}], "+",
                                                                                RowBox[{"{",
                                                                                        RowBox[{"dx", ",", "dy"}],
                                                                                        "}"}]}]}], "}"}], "]"}],
                                                        ",",
                                                        RowBox[{"Line", "[",
                                                                RowBox[{"{",
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                "e", "\[LeftDoubleBracket]", "2",
                                                                                "\[RightDoubleBracket]"}], ",",
                                                                            RowBox[{
                                                                                RowBox[{
                                                                                    "e", "\[LeftDoubleBracket]", "2",
                                                                                    "\[RightDoubleBracket]"}], "-",
                                                                                RowBox[{"{",
                                                                                        RowBox[{"dx", ",", "dy"}],
                                                                                        "}"}]}]}], "}"}], "]"}]}],
                                                "}"}]}], ",",
                                    RowBox[{"{",
                                            RowBox[{
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{
                                                                RowBox[{"-", "1"}], "===", "color2"}], ",", "color1",
                                                            ",",
                                                            "color2"}], "]"}], ",", " ",
                                                RowBox[{"Line", "[", "e", "]"}]}], "}"}]}], "]"}]}]}],
                "\[IndentingNewLine]", "]"}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.787062472954484 * ^ 9}, 3.788641593916823 * ^ 9},
CellLabel->"In[9]:=",
CellID->1195378936],

Cell[BoxData[
    RowBox[{
        RowBox[{"toroidPt", "[",
                RowBox[{"e_", ",", "frac_"}], "]"}], ":=",
        RowBox[{"Module", "[",
                RowBox[{
                    RowBox[{"{",
                            RowBox[{
                                "dx", ",", "dy", ",", "dx2", ",", "dy2", ",", "dist", ",",
                                "pt"}], "}"}], ",", "\[IndentingNewLine]",
                    RowBox[{
                        RowBox[{"dx", " ", "=", " ",
                                RowBox[{"Abs", "[",
                                        RowBox[{
                                            RowBox[{"e", "\[LeftDoubleBracket]",
                                                    RowBox[{"2", ",", "1"}], "\[RightDoubleBracket]"}], "-",
                                            RowBox[{"e", "\[LeftDoubleBracket]",
                                                    RowBox[{"1", ",", "1"}], "\[RightDoubleBracket]"}]}],
                                        "]"}]}], ";", "\[IndentingNewLine]",
                        RowBox[{"dy", " ", "=", " ",
                                RowBox[{"Abs", "[",
                                        RowBox[{
                                            RowBox[{"e", "\[LeftDoubleBracket]",
                                                    RowBox[{"2", ",", "2"}], "\[RightDoubleBracket]"}], "-",
                                            RowBox[{"e", "\[LeftDoubleBracket]",
                                                    RowBox[{"1", ",", "2"}], "\[RightDoubleBracket]"}]}],
                                        "]"}]}], ";", "\[IndentingNewLine]",
                        RowBox[{"dx2", " ", "=",
                                RowBox[{
                                    RowBox[{"e", "\[LeftDoubleBracket]",
                                            RowBox[{"2", ",", "1"}], "\[RightDoubleBracket]"}], "-",
                                    RowBox[{"e", "\[LeftDoubleBracket]",
                                            RowBox[{"1", ",", "1"}], "\[RightDoubleBracket]"}], "+",
                                    RowBox[{"If", "[",
                                            RowBox[{
                                                RowBox[{"dx", "<",
                                                        RowBox[{
                                                            RowBox[{"2", "\[Pi]"}], "-", " ", "dx"}]}], ",", "0", ",",
                                                " ",
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{
                                                                RowBox[{"e", "\[LeftDoubleBracket]",
                                                                        RowBox[{"2", ",", "1"}],
                                                                        "\[RightDoubleBracket]"}], ">",

                                                                RowBox[{"e", "\[LeftDoubleBracket]",
                                                                        RowBox[{"1", ",", "1"}],
                                                                        "\[RightDoubleBracket]"}]}],
                                                            ",",
                                                            RowBox[{
                                                                RowBox[{"-", "2"}], "\[Pi]"}], ",",
                                                            RowBox[{
                                                                RowBox[{"+", "2"}], "\[Pi]"}]}], "]"}]}], "]"}]}]}],
                        ";",
                        "\[IndentingNewLine]",
                        RowBox[{"dy2", " ", "=",
                                RowBox[{
                                    RowBox[{"e", "\[LeftDoubleBracket]",
                                            RowBox[{"2", ",", "2"}], "\[RightDoubleBracket]"}], "-",
                                    RowBox[{"e", "\[LeftDoubleBracket]",
                                            RowBox[{"1", ",", "2"}], "\[RightDoubleBracket]"}], "+",
                                    RowBox[{"If", "[",
                                            RowBox[{
                                                RowBox[{"dy", "<",
                                                        RowBox[{
                                                            RowBox[{"2", "\[Pi]"}], "-", " ", "dy"}]}], " ", ",", "0",
                                                ",", " ",
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{
                                                                RowBox[{"e", "\[LeftDoubleBracket]",
                                                                        RowBox[{"2", ",", "2"}],
                                                                        "\[RightDoubleBracket]"}], ">",

                                                                RowBox[{"e", "\[LeftDoubleBracket]",
                                                                        RowBox[{"1", ",", "2"}],
                                                                        "\[RightDoubleBracket]"}]}],
                                                            ",",
                                                            RowBox[{
                                                                RowBox[{"-", "2"}], "\[Pi]"}], ",",
                                                            RowBox[{
                                                                RowBox[{"+", "2"}], "\[Pi]"}]}], "]"}]}], "]"}]}]}],
                        ";",
                        "\[IndentingNewLine]",
                        RowBox[{"dist", " ", "=",
                                SqrtBox[
                                    RowBox[{
                                        SuperscriptBox["dx2", "2"], "+",
                                        SuperscriptBox["dy2", "2"]}]]}], ";", "\[IndentingNewLine]",
                        RowBox[{"If", "[",
                                RowBox[{
                                    RowBox[{"dist", "\[Equal]", "0"}], ",",
                                    RowBox[{"pt", "=",
                                            RowBox[{
                                                "e", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}]}],
                                    ",", "\[IndentingNewLine]",
                                    RowBox[{
                                        RowBox[{"pt", "=",
                                                RowBox[{
                                                    RowBox[{
                                                        "e", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                                    "+",
                                                    RowBox[{"frac",
                                                            RowBox[{"{",
                                                                    RowBox[{"dx2", ",", "dy2"}], "}"}]}]}]}], ";",
                                        "\[IndentingNewLine]",
                                        RowBox[{
                                            RowBox[{
                                                "pt", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                            " ", "=",
                                            RowBox[{
                                                RowBox[{
                                                    "pt", "\[LeftDoubleBracket]", "1",
                                                    "\[RightDoubleBracket]"}], "+",
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{
                                                                RowBox[{
                                                                    "pt", "\[LeftDoubleBracket]", "1",
                                                                    "\[RightDoubleBracket]"}], ">",
                                                                RowBox[{"2", "\[Pi]"}]}], ",",
                                                            RowBox[{
                                                                RowBox[{"-", "2"}], "\[Pi]"}], ",",
                                                            RowBox[{"If", "[",
                                                                    RowBox[{
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                "pt", "\[LeftDoubleBracket]", "1",
                                                                                "\[RightDoubleBracket]"}], "<", "0"}],
                                                                        ",",
                                                                        RowBox[{"2", "\[Pi]"}], ",", "0"}], "]"}]}],
                                                        "]"}]}]}],
                                        ";", "\[IndentingNewLine]",
                                        RowBox[{
                                            RowBox[{
                                                "pt", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                            " ", "=",
                                            RowBox[{
                                                RowBox[{
                                                    "pt", "\[LeftDoubleBracket]", "2",
                                                    "\[RightDoubleBracket]"}], "+",
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{
                                                                RowBox[{
                                                                    "pt", "\[LeftDoubleBracket]", "2",
                                                                    "\[RightDoubleBracket]"}], ">",
                                                                RowBox[{"2", "\[Pi]"}]}], ",",
                                                            RowBox[{
                                                                RowBox[{"-", "2"}], "\[Pi]"}], ",",
                                                            RowBox[{"If", "[",
                                                                    RowBox[{
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                "pt", "\[LeftDoubleBracket]", "2",
                                                                                "\[RightDoubleBracket]"}], "<", "0"}],
                                                                        ",",
                                                                        RowBox[{"2", "\[Pi]"}], ",", "0"}], "]"}]}],
                                                        "]"}]}]}],
                                        ";"}]}], "\[IndentingNewLine]", "]"}], ";",
                        "\[IndentingNewLine]", "pt"}]}], "\[IndentingNewLine]",
                "]"}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.787062479434539 * ^ 9}, 3.7886415939168663
` * ^ 9},
CellLabel->"In[10]:=",
CellID->844859229],

Cell[BoxData[
    RowBox[{
        RowBox[{"loc", "[", "col_", "]"}], ":=",
        RowBox[{"(*", " ",
                RowBox[{"a", " ", "colored", " ", "locator", " ", "icon"}], "*)"}],
        RowBox[{"ToExpression", "@",
                RowBox[{"GraphicsBox", "[",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"col", ",",
                                            RowBox[{"{",
                                                    RowBox[{
                                                        RowBox[{"AbsoluteThickness", "[", "1", "]"}], ",",
                                                        RowBox[{"Antialiasing", "\[Rule]", "False"}], ",",
                                                        RowBox[{"LineBox", "[",
                                                                RowBox[{"{",
                                                                        RowBox[{
                                                                            RowBox[{"{",
                                                                                    RowBox[{
                                                                                        RowBox[{"{",
                                                                                                RowBox[{"0", ",",
                                                                                                        RowBox[{"-",
                                                                                                                "10"}]}],
                                                                                                "}"}], ",",
                                                                                        RowBox[{"{",
                                                                                                RowBox[{"0", ",",
                                                                                                        RowBox[{"-",
                                                                                                                "2"}]}],
                                                                                                "}"}]}], "}"}], ",",
                                                                            RowBox[{"{",
                                                                                    RowBox[{
                                                                                        RowBox[{"{",
                                                                                                RowBox[{"0", ",", "2"}],
                                                                                                "}"}], ",",
                                                                                        RowBox[{"{",
                                                                                                RowBox[
                                                                                                    {"0", ",", "10"}],
                                                                                                "}"}]}], "}"}], ",",
                                                                            RowBox[{"{",
                                                                                    RowBox[{
                                                                                        RowBox[{"{",
                                                                                                RowBox[{
                                                                                                    RowBox[{"-", "10"}],
                                                                                                    ",", "0"}], "}"}],
                                                                                        ",",
                                                                                        RowBox[{"{",
                                                                                                RowBox[{
                                                                                                    RowBox[{"-", "2"}],
                                                                                                    ",", "0"}], "}"}]}],
                                                                                    "}"}], ",",
                                                                            RowBox[{"{",
                                                                                    RowBox[{
                                                                                        RowBox[{"{",
                                                                                                RowBox[{"2", ",", "0"}],
                                                                                                "}"}], ",",
                                                                                        RowBox[{"{",
                                                                                                RowBox[
                                                                                                    {"10", ",", "0"}],
                                                                                                "}"}]}], "}"}]}], "}"}],
                                                                "]"}], ",",
                                                        RowBox[{"Antialiasing", "\[Rule]", "True"}], ",",
                                                        RowBox[{"CircleBox", "[",
                                                                RowBox[{
                                                                    RowBox[{"{",
                                                                            RowBox[{
                                                                                RowBox[{"-", "0.5"}], ",", "0.5"}],
                                                                            "}"}], ",", "5"}],
                                                                "]"}]}], "}"}], ",",
                                            RowBox[{"{",
                                                    RowBox[{
                                                        RowBox[{"AbsoluteThickness", "[", "3", "]"}], ",",
                                                        RowBox[{"Opacity", "[", "0.3", "]"}], ",",
                                                        RowBox[{"CircleBox", "[",
                                                                RowBox[{
                                                                    RowBox[{"{",
                                                                            RowBox[{
                                                                                RowBox[{"-", "0.5"}], ",", "0.5"}],
                                                                            "}"}], ",", "3"}],
                                                                "]"}]}], "}"}]}], "}"}], ",",
                            RowBox[{"ImageSize", "\[Rule]", "17"}], ",",
                            RowBox[{"PlotRange", "\[Rule]",
                                    RowBox[{"{",
                                            RowBox[{
                                                RowBox[{"{",
                                                        RowBox[{
                                                            RowBox[{"-", "8"}], ",", "8"}], "}"}], ",",
                                                RowBox[{"{",
                                                        RowBox[{
                                                            RowBox[{"-", "8"}], ",", "8"}], "}"}]}], "}"}]}]}],
                        "]"}]}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.7870624874213753` * ^ 9}, 3.788641593916926 * ^ 9},
CellLabel->"In[11]:=",
CellID->937387871],

Cell[BoxData[
    RowBox[{
        RowBox[{"(*",
                RowBox[{
                    "augments", " ", "the", " ", "list", " ", "of", " ", "edges", " ",
                    "in", " ", "a", " ", "graph", " ", "of", " ", "points"}], "*)"}],
        "\[IndentingNewLine]",
        RowBox[{
            RowBox[{"connectPoints", "[",
                    RowBox[{
                        "goodPts_", ",", "edgesNNadjin_", ",", "polys_", ",", "delta_",
                        ",", "edgesNNin_", ",", " ", "point2start_", ",", "r_"}], "]"}],
            ":=", "\[IndentingNewLine]",
            RowBox[{"Module", "[",
                    RowBox[{
                        RowBox[{"{",
                                RowBox[{
                                    "ps", ",", "pe", ",", "pei", ",", "\[IndentingNewLine]",
                                    "edgesNNadj", ",", "\[IndentingNewLine]", "edgesNN"}],
                                "\[IndentingNewLine]", "}"}], ",", "\[IndentingNewLine]",
                        RowBox[{
                            RowBox[{"edgesNNadj", "=", "edgesNNadjin"}], ";",
                            "\[IndentingNewLine]",
                            RowBox[{"edgesNN", "=", "edgesNNin"}], ";",
                            "\[IndentingNewLine]",
                            RowBox[{"Table", "[", "\[IndentingNewLine]",
                                    RowBox[{
                                        RowBox[{
                                            RowBox[{"ps", " ", "=", " ",
                                                    RowBox[{
                                                        "goodPts", "\[LeftDoubleBracket]", "i",
                                                        "\[RightDoubleBracket]"}]}], ";", "\[IndentingNewLine]",
                                            RowBox[{"Table", "[", "\[IndentingNewLine]",
                                                    RowBox[{
                                                        RowBox[{
                                                            RowBox[{"pei", " ", "=", " ",
                                                                    RowBox[{
                                                                        RowBox[{"Position", "[",
                                                                                RowBox[{"goodPts", ",", "pe", ",", "1",
                                                                                        ",", "1"}],
                                                                                "]"}], "\[LeftDoubleBracket]",
                                                                        RowBox[{"1", ",", "1"}],
                                                                        "\[RightDoubleBracket]"}]}],
                                                            ";", "\[IndentingNewLine]",
                                                            RowBox[{"(*",
                                                                    RowBox[{
                                                                        "if", " ", "pei", " ", "is", " ", "not", " ",
                                                                        "in", " ",

                                                                        RowBox[{
                                                                            "edgesNNadj", "\[LeftDoubleBracket]", "i",
                                                                            "\[RightDoubleBracket]"}]}], " ", "*)"}],
                                                            "\[IndentingNewLine]",
                                                            RowBox[{"If", "[", " ",
                                                                    RowBox[{
                                                                        RowBox[{
                                                                            RowBox[{"Count", "[",
                                                                                    RowBox[{
                                                                                        RowBox[{
                                                                                            "edgesNNadj",
                                                                                            "\[LeftDoubleBracket]", "i",
                                                                                            "\[RightDoubleBracket]"}],
                                                                                        ",", "pei"}], "]"}], "<",
                                                                            "1"}], ",", "\[IndentingNewLine]",
                                                                        RowBox[{"If", "[",
                                                                                RowBox[{
                                                                                    RowBox[{"pathOKT", "[",
                                                                                            RowBox[{
                                                                                                "ps", ",", "pe", ",",
                                                                                                "polys", ",", "delta"}],
                                                                                            "]"}],
                                                                                    ",", " ", "\[IndentingNewLine]",
                                                                                    RowBox[{
                                                                                        RowBox[{"AppendTo", "[",
                                                                                                RowBox[{"edgesNN", ",",
                                                                                                        RowBox[{"{",
                                                                                                                RowBox[{
                                                                                                                    "ps",
                                                                                                                    ",",
                                                                                                                    "pe"}],
                                                                                                                "}"}]}],
                                                                                                "]"}], ";",
                                                                                        "\[IndentingNewLine]",
                                                                                        RowBox[{"AppendTo", "[",
                                                                                                RowBox[{
                                                                                                    RowBox[{
                                                                                                        "edgesNNadj",
                                                                                                        "\[LeftDoubleBracket]",
                                                                                                        "i",
                                                                                                        "\[RightDoubleBracket]"}],
                                                                                                    ",", "pei"}], "]"}],
                                                                                        ";", "\[IndentingNewLine]",
                                                                                        RowBox[{"AppendTo", "[",
                                                                                                RowBox[{
                                                                                                    RowBox[{
                                                                                                        "edgesNNadj",
                                                                                                        "\[LeftDoubleBracket]",
                                                                                                        "pei",
                                                                                                        "\[RightDoubleBracket]"}],
                                                                                                    ",", "i"}], "]"}],
                                                                                        ";"}]}], "]"}]}],
                                                                    "\[IndentingNewLine]", "]"}]}],
                                                        " ", ",",
                                                        RowBox[{"{",
                                                                RowBox[{"pe", ",",
                                                                        RowBox[{"Quiet", "[",
                                                                                RowBox[{"Nearest", "[",
                                                                                        RowBox[{
                                                                                            RowBox[{"Drop", "[",
                                                                                                    RowBox[
                                                                                                        {"goodPts", ",",
                                                                                                         RowBox[
                                                                                                             {"{", "i",
                                                                                                              "}"}]}],
                                                                                                    "]"}], ",", "ps",
                                                                                            ",",
                                                                                            RowBox[{"{",
                                                                                                    RowBox[{"10", ",",
                                                                                                            "r"}],
                                                                                                    "}"}], ",",
                                                                                            RowBox[{
                                                                                                "DistanceFunction",
                                                                                                "\[Rule]",
                                                                                                "toroidDist"}]}],
                                                                                        "]"}], "]"}]}], "}"}]}],
                                                    "]"}]}], ",",
                                        "\[IndentingNewLine]", " ",
                                        RowBox[{"{",
                                                RowBox[{"i", ",", "point2start", ",",
                                                        RowBox[{"Length", "[", "goodPts", "]"}]}], "}"}]}], "]"}],
                            ";", "\[IndentingNewLine]",
                            RowBox[{"{",
                                    RowBox[{"edgesNNadj", ",", "edgesNN"}], "}"}]}]}],
                    "\[IndentingNewLine]", "]"}]}]}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
InitializationCell->True,
CellChangeTimes->{{3.783700792983756 * ^ 9, 3.783700821655879 * ^ 9}, {
    3.783705041306859 * ^ 9, 3.783705041890811 * ^ 9}, {3.785500256930531 * ^ 9,
                                                        3.78550027576088 * ^ 9}, {3.785500497667341 * ^ 9,
                                                                                  3.785500503613709 * ^ 9},
                  {3.78550056342974 * ^ 9,
                   3.785500579331963 * ^ 9}, {3.785500774563938 * ^ 9,
                                              3.785500791390098 * ^ 9}, 3.785693271019761 * ^ 9,
                  {3.785693731813908 * ^ 9,
                   3.7856938876730947` * ^ 9}, {3.785694138261951 * ^ 9,
                                                3.785694181427334 * ^ 9}, {3.78569444464602 * ^ 9,
                                                                           3.785694444826344 * ^ 9},
                  {3.785696322280609 * ^ 9,
                   3.7856963344036016` * ^ 9}, {3.785860960361641 * ^ 9,
                                                3.7858609669782753` * ^ 9}, {3.785872603945973 * ^ 9,
                                                                             3.7858726352158737` * ^ 9},
                  3.785872673954473 * ^ 9, {
                      3.787013369984475 * ^ 9, 3.787013508539174 * ^ 9}, {3.787013555647184 * ^ 9,
                                                                          3.787013622830385 * ^ 9}, {3.7870624088469133
                  ` * ^ 9,
                  3.7870624874213753` * ^ 9}, 3.787062866370577 * ^ 9,
                                              3.788641593916992 * ^ 9},
CellLabel->"In[12]:=",
CellID->894093768],

Cell[BoxData[
    RowBox[{"Manipulate", "[",
            RowBox[{
                RowBox[{"Module", "[",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"qsni", ",", "qfni", ",",
                                            RowBox[{"qsn", "=",
                                                    RowBox[{"{", "}"}]}], ",",
                                            RowBox[{"qfn", " ", "=", " ",
                                                    RowBox[{"{", "}"}]}], ",",
                                            RowBox[{"delta", " ", "=", " ", ".1"}], ",", "totdist"}],
                                    "}"}], ",", "\[IndentingNewLine]",
                            RowBox[{
                                RowBox[{"If", "[",
                                        RowBox[{"restart", ",", "\[IndentingNewLine]",
                                                RowBox[{
                                                    RowBox[{"restart", "=", "False"}], ";",
                                                    "\[IndentingNewLine]",
                                                    RowBox[{"polyN", " ", "=", " ", "4"}], ";",
                                                    "\[IndentingNewLine]",
                                                    RowBox[{"polySides", " ", "=", " ",
                                                            RowBox[{"RandomInteger", "[",
                                                                    RowBox[{
                                                                        RowBox[{"{",
                                                                                RowBox[{"3", ",", "7"}], "}"}], ",",
                                                                        "polyN"}], "]"}]}],
                                                    ";", "\[IndentingNewLine]",
                                                    RowBox[{"polys", " ", "=", " ",
                                                            RowBox[{"CirclePoints", "/@", "polySides"}]}], ";",
                                                    RowBox[{"(*",
                                                            RowBox[{"some", " ", "regular", " ", "polygons"}], "*)"}],
                                                    "\[IndentingNewLine]",
                                                    RowBox[{"polyXY", " ", "=", " ",
                                                            RowBox[{"RandomReal", "[",
                                                                    RowBox[{
                                                                        RowBox[{"{",
                                                                                RowBox[{"0", ",",
                                                                                        RowBox[{"2", "\[Pi]"}]}], "}"}],
                                                                        ",",
                                                                        RowBox[{"{",
                                                                                RowBox[{"polyN", ",", "2"}], "}"}]}],
                                                                    "]"}]}], ";",
                                                    RowBox[{"(*",
                                                            RowBox[{
                                                                "shift", " ", "polygons", " ", "to", " ", "random", " ",
                                                                "coordinates"}], "*)"}], "\[IndentingNewLine]",
                                                    RowBox[{"polys", " ", "=", " ",
                                                            RowBox[{"Table", "[",
                                                                    RowBox[{
                                                                        RowBox[{
                                                                            RowBox[{
                                                                                RowBox[{"(",
                                                                                        RowBox[{
                                                                                            RowBox[{
                                                                                                "polyXY",
                                                                                                "\[LeftDoubleBracket]",
                                                                                                "i",
                                                                                                "\[RightDoubleBracket]"}],
                                                                                            "+", "#"}], ")"}], "&"}],
                                                                            "/@",
                                                                            RowBox[{
                                                                                "polys", "\[LeftDoubleBracket]", "i",
                                                                                "\[RightDoubleBracket]"}]}], ",",
                                                                        RowBox[{"{",
                                                                                RowBox[{"i", ",", "1", ",", "polyN"}],
                                                                                "}"}]}], "]"}]}],
                                                    ";", "\[IndentingNewLine]",
                                                    RowBox[{"badPts", "=",
                                                            RowBox[{"{", "}"}]}], ";", "\[IndentingNewLine]",
                                                    RowBox[{"goodPts", "=",
                                                            RowBox[{"{", "}"}]}], ";", "\[IndentingNewLine]",
                                                    RowBox[{"pts", " ", "=", " ",
                                                            RowBox[{"{", "}"}]}], ";", "\[IndentingNewLine]",
                                                    RowBox[{"edgesNN", " ", "=", " ",
                                                            RowBox[{"{", "}"}]}], ";", "\[IndentingNewLine]",
                                                    RowBox[{"edgesNNadj", " ", "=",
                                                            RowBox[{"{", "}"}]}], ";"}]}], "\[IndentingNewLine]", "]"}],
                                ";", "\[IndentingNewLine]",
                                RowBox[{"(*",
                                        RowBox[{
                                            "Toroid", " ", "assumption", " ", "wraps", " ", "locators",
                                            " ", "across", " ",
                                            RowBox[{"boundary", "."}]}], "*)"}], "\[IndentingNewLine]",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    "qs", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                                "<", "0"}], ",", " ",
                                            RowBox[{
                                                RowBox[{
                                                    "qs", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                                "=",
                                                RowBox[{"2", "\[Pi]"}]}]}], "]"}], ";",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    "qs", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                                ">",
                                                RowBox[{"2", "\[Pi]"}]}], ",",
                                            RowBox[{
                                                RowBox[{
                                                    "qs", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                                "=", "0"}]}], "]"}], ";", "\[IndentingNewLine]",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    "qs", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                                "<", "0"}], ",", " ",
                                            RowBox[{
                                                RowBox[{
                                                    "qs", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                                "=",
                                                RowBox[{"2", "\[Pi]"}]}]}], "]"}], ";",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    "qs", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                                ">",
                                                RowBox[{"2", "\[Pi]"}]}], ",",
                                            RowBox[{
                                                RowBox[{
                                                    "qs", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                                "=", "0"}]}], "]"}], ";", "\[IndentingNewLine]",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    "qf", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                                "<", "0"}], ",", " ",
                                            RowBox[{
                                                RowBox[{
                                                    "qf", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                                "=",
                                                RowBox[{"2", "\[Pi]"}]}]}], "]"}], ";",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    "qf", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                                ">",
                                                RowBox[{"2", "\[Pi]"}]}], ",",
                                            RowBox[{
                                                RowBox[{
                                                    "qf", "\[LeftDoubleBracket]", "1", "\[RightDoubleBracket]"}],
                                                "=", "0"}]}], "]"}], ";", "\[IndentingNewLine]",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    "qf", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                                "<", "0"}], ",", " ",
                                            RowBox[{
                                                RowBox[{
                                                    "qf", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                                "=",
                                                RowBox[{"2", "\[Pi]"}]}]}], "]"}], ";",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    "qf", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                                ">",
                                                RowBox[{"2", "\[Pi]"}]}], ",",
                                            RowBox[{
                                                RowBox[{
                                                    "qf", "\[LeftDoubleBracket]", "2", "\[RightDoubleBracket]"}],
                                                "=", "0"}]}], "]"}], ";", "\[IndentingNewLine]",
                                "\[IndentingNewLine]",
                                RowBox[{"If", "[",
                                        RowBox[{"addPoints", ",", "\[IndentingNewLine]",
                                                RowBox[{
                                                    RowBox[{"addPoints", " ", "=", " ", "False"}], ";",
                                                    "\[IndentingNewLine]",
                                                    RowBox[{"Module", "[",
                                                            RowBox[{
                                                                RowBox[{"{",
                                                                        RowBox[{"newpts", ",", "point2start"}], "}"}],
                                                                ",",
                                                                "\[IndentingNewLine]",
                                                                RowBox[{
                                                                    RowBox[{"point2start", " ", "=", " ",
                                                                            RowBox[{
                                                                                RowBox[{"Length", "[", "goodPts", "]"}],
                                                                                "+", "1"}]}],
                                                                    ";", "\[IndentingNewLine]",
                                                                    RowBox[{"(*", " ",
                                                                            RowBox[{"generate", " ", "random", " ",
                                                                                    "points"}], " ",
                                                                            "*)"}], "\[IndentingNewLine]",
                                                                    RowBox[{"newpts", "=",
                                                                            RowBox[{"RandomReal", "[",
                                                                                    RowBox[{
                                                                                        RowBox[{"{",
                                                                                                RowBox[{"0", ",",
                                                                                                        RowBox[{"2",
                                                                                                                "\[Pi]"}]}],
                                                                                                "}"}], ",",
                                                                                        RowBox[{"{",
                                                                                                RowBox[
                                                                                                    {"50", ",", "2"}],
                                                                                                "}"}]}], "]"}]}], ";",
                                                                    "\[IndentingNewLine]",
                                                                    RowBox[{"pts", " ", "=", " ",
                                                                            RowBox[{"Join", "[",
                                                                                    RowBox[{"pts", ",", "newpts"}],
                                                                                    "]"}]}], ";",
                                                                    "\[IndentingNewLine]", " ",
                                                                    RowBox[{"Table", "[", "\[IndentingNewLine]",
                                                                            RowBox[{
                                                                                RowBox[{"If", "[",
                                                                                        RowBox[{
                                                                                            RowBox[{"ptInPolys", "[",
                                                                                                    RowBox[
                                                                                                        {"polys", ",",
                                                                                                         RowBox[{
                                                                                                             "newpts",
                                                                                                             "\[LeftDoubleBracket]",
                                                                                                             "i",
                                                                                                             "\[RightDoubleBracket]"}]}],
                                                                                                    "]"}], ",",
                                                                                            "\[IndentingNewLine]",
                                                                                            RowBox[{"AppendTo", "[",
                                                                                                    RowBox[
                                                                                                        {"badPts", ",",
                                                                                                         RowBox[{
                                                                                                             "newpts",
                                                                                                             "\[LeftDoubleBracket]",
                                                                                                             "i",
                                                                                                             "\[RightDoubleBracket]"}]}],
                                                                                                    "]"}], ",",
                                                                                            "\[IndentingNewLine]",
                                                                                            RowBox[{"AppendTo", "[",
                                                                                                    RowBox[
                                                                                                        {"goodPts", ",",
                                                                                                         RowBox[{
                                                                                                             "newpts",
                                                                                                             "\[LeftDoubleBracket]",
                                                                                                             "i",
                                                                                                             "\[RightDoubleBracket]"}]}],
                                                                                                    "]"}]}], "]"}], ",",
                                                                                "\[IndentingNewLine]",
                                                                                RowBox[{"{",
                                                                                        RowBox[{"i", ",", "1", ",",
                                                                                                RowBox[{"Length", "[",
                                                                                                        "newpts",
                                                                                                        "]"}]}],
                                                                                        "}"}]}],
                                                                            "]"}], ";", "\[IndentingNewLine]",
                                                                    RowBox[{"(*", " ",
                                                                            RowBox[{
                                                                                "update", " ", "the", " ", "connected",
                                                                                " ", "points"}],
                                                                            " ", "*)"}], "\[IndentingNewLine]",
                                                                    RowBox[{"If", "[", " ",
                                                                            RowBox[{
                                                                                RowBox[{
                                                                                    RowBox[{"Length", "[", "goodPts",
                                                                                            "]"}], " ", ">", " ",
                                                                                    RowBox[{"point2start", "-", "1"}]}],
                                                                                ",",
                                                                                "\[IndentingNewLine]",
                                                                                RowBox[{
                                                                                    RowBox[{"edgesNNadj", " ", "=",
                                                                                            RowBox[{"Join", "[",
                                                                                                    RowBox[
                                                                                                        {"edgesNNadj",
                                                                                                         ",",
                                                                                                         RowBox[{
                                                                                                             "ConstantArray",
                                                                                                             "[",
                                                                                                             RowBox[{
                                                                                                                 RowBox[
                                                                                                                     {
                                                                                                                         "{",
                                                                                                                         "}"}],
                                                                                                                 ",",
                                                                                                                 RowBox[
                                                                                                                     {
                                                                                                                         RowBox[
                                                                                                                             {
                                                                                                                                 "Length",
                                                                                                                                 "[",
                                                                                                                                 "goodPts",
                                                                                                                                 "]"}],
                                                                                                                         "-",
                                                                                                                         "point2start",
                                                                                                                         "+",
                                                                                                                         "1"}]}],
                                                                                                             "]"}]}],
                                                                                                    "]"}]}],
                                                                                    ";", "\[IndentingNewLine]",
                                                                                    RowBox[{"If", "[",
                                                                                            RowBox[{
                                                                                                RowBox[{"r", ">", "0"}],
                                                                                                ",",
                                                                                                RowBox[{
                                                                                                    RowBox[{"{",
                                                                                                            RowBox[{
                                                                                                                "edgesNNadj",
                                                                                                                ",",
                                                                                                                "edgesNN"}],
                                                                                                            "}"}], "=",
                                                                                                    RowBox[{
                                                                                                        "connectPoints",
                                                                                                        "[",
                                                                                                        RowBox[{
                                                                                                            "goodPts",
                                                                                                            ",",
                                                                                                            "edgesNNadj",
                                                                                                            ",",
                                                                                                            "polys",
                                                                                                            ",",
                                                                                                            "delta",
                                                                                                            ",",
                                                                                                            "edgesNN",
                                                                                                            ",",
                                                                                                            "point2start",
                                                                                                            " ",
                                                                                                            ",", "r"}],
                                                                                                        "]"}]}]}],
                                                                                            "]"}]}]}], "]"}], ";"}]}],
                                                            "\[IndentingNewLine]", "]"}]}]}], "]"}], ";",
                                "\[IndentingNewLine]", "\[IndentingNewLine]",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{"r", "\[NotEqual]", " ", "rold"}], " ", "&&", " ",
                                                RowBox[{
                                                    RowBox[{"Length", "[", "goodPts", "]"}], ">", "5"}]}], " ",
                                            ",", "\[IndentingNewLine]",
                                            RowBox[{
                                                RowBox[{"rold", " ", "=", " ", "r"}], ";",
                                                "\[IndentingNewLine]",
                                                RowBox[{"edgesNN", " ", "=", " ",
                                                        RowBox[{"{", "}"}]}], ";", "\[IndentingNewLine]",
                                                RowBox[{"edgesNNadj", " ", "=",
                                                        RowBox[{"ConstantArray", "[",
                                                                RowBox[{
                                                                    RowBox[{"{", "}"}], ",",
                                                                    RowBox[{"Length", "[", "goodPts", "]"}]}], "]"}]}],
                                                ";",
                                                "\[IndentingNewLine]",
                                                RowBox[{"(*", " ",
                                                        RowBox[{"Build", " ", "an", " ", "adjacency", " ",
                                                                RowBox[{"list", ":"}]}], " ", "*)"}],
                                                "\[IndentingNewLine]",
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{"r", ">", "0"}], ",", "\[IndentingNewLine]",
                                                            RowBox[{
                                                                RowBox[{
                                                                    RowBox[{"{",
                                                                            RowBox[{"edgesNNadj", ",", "edgesNN"}],
                                                                            "}"}], "=",
                                                                    RowBox[{"connectPoints", "[",
                                                                            RowBox[{
                                                                                "goodPts", ",", "edgesNNadj", ",",
                                                                                "polys", ",",
                                                                                "delta", ",", "edgesNN", ",", " ", "1",
                                                                                ",", "r"}],
                                                                            "]"}]}], ";"}]}], "\[IndentingNewLine]",
                                                        "]"}]}]}],
                                        "]"}], ";", "\[IndentingNewLine]",
                                RowBox[{"(*", " ",
                                        RowBox[{
                                            "Check", " ", "if", " ", "we", " ", "can", " ", "go", " ",
                                            "straight", " ", "from", " ", "qs", " ", "to", " ",
                                            RowBox[{"qf", ":"}]}], " ", "*)"}], "\[IndentingNewLine]",
                                RowBox[{"path", "=",
                                        RowBox[{"-", "1"}]}], ";", "\[IndentingNewLine]",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{
                                                    RowBox[{"toroidDist", "[",
                                                            RowBox[{"qs", ",", "qf"}], "]"}], "<", "r"}], "&&", " ",
                                                RowBox[{"pathOKT", "[",
                                                        RowBox[{"qs", ",", "qf", ",", "polys", ",", "delta"}],
                                                        "]"}]}], ",", "\[IndentingNewLine]",
                                            RowBox[{"path", "=",
                                                    RowBox[{"-", "2"}]}], ",", "\[IndentingNewLine]",
                                            RowBox[{
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{
                                                                RowBox[{"!",
                                                                        RowBox[{"ptInPolys", "[",
                                                                                RowBox[{"polys", ",", "qs"}], "]"}]}],
                                                                "&&",
                                                                RowBox[{
                                                                    RowBox[{"Length", "[", "goodPts", "]"}], ">",
                                                                    "5"}]}],
                                                            ",", "\[IndentingNewLine]",
                                                            RowBox[{"(*", " ",
                                                                    RowBox[{
                                                                        "Connect", " ", "qs", " ", "to", " ", "the",
                                                                        " ",
                                                                        RowBox[{"map", ":"}]}], " ", "*)"}],
                                                            "\[IndentingNewLine]",
                                                            RowBox[{"Do", "[",
                                                                    RowBox[{
                                                                        RowBox[{"If", "[",
                                                                                RowBox[{
                                                                                    RowBox[{"pathOKT", "[",
                                                                                            RowBox[
                                                                                                {"qs", ",", "pe", ",",
                                                                                                 "polys", ",",
                                                                                                 "delta"}],
                                                                                            "]"}], ",",
                                                                                    RowBox[{
                                                                                        RowBox[{"qsn", " ", "=", " ",
                                                                                                "pe"}], ";",
                                                                                        RowBox[{"Break", "[", "]"}]}]}],
                                                                                " ", "]"}], ",",
                                                                        "\[IndentingNewLine]",
                                                                        RowBox[{"{",
                                                                                RowBox[{"pe", ",", " ",
                                                                                        RowBox[{"Quiet", "[",
                                                                                                RowBox[{"Nearest", "[",
                                                                                                        RowBox[
                                                                                                            {"goodPts",
                                                                                                             ",", "qs",
                                                                                                             ",", "1",
                                                                                                             ",",
                                                                                                             RowBox[{
                                                                                                                 "DistanceFunction",
                                                                                                                 "\[Rule]",
                                                                                                                 "toroidDist"}]}],
                                                                                                        "]"}], "]"}]}],
                                                                                "}"}]}], "]"}]}], "]"}], ";",
                                                "\[IndentingNewLine]", "\[IndentingNewLine]",
                                                RowBox[{"If", "[",
                                                        RowBox[{
                                                            RowBox[{
                                                                RowBox[{"!",
                                                                        RowBox[{"ptInPolys", "[",
                                                                                RowBox[{"polys", ",", "qf"}], "]"}]}],
                                                                "&&",
                                                                RowBox[{
                                                                    RowBox[{"Length", "[", "goodPts", "]"}], ">",
                                                                    "5"}]}],
                                                            ",", "\[IndentingNewLine]",
                                                            RowBox[{"(*", " ",
                                                                    RowBox[{
                                                                        "Connect", " ", "qf", " ", "to", " ", "the",
                                                                        " ",
                                                                        RowBox[{"map", ":"}]}], " ", "*)"}],
                                                            "\[IndentingNewLine]",
                                                            RowBox[{"Do", "[",
                                                                    RowBox[{
                                                                        RowBox[{"If", "[",
                                                                                RowBox[{
                                                                                    RowBox[{"pathOKT", "[",
                                                                                            RowBox[
                                                                                                {"qf", ",", "pe", ",",
                                                                                                 "polys", ",",
                                                                                                 "delta"}],
                                                                                            "]"}], ",",
                                                                                    RowBox[{
                                                                                        RowBox[{"qfn", " ", "=", " ",
                                                                                                "pe"}], ";",
                                                                                        RowBox[{"Break", "[", "]"}]}]}],
                                                                                " ", "]"}], ",",
                                                                        "\[IndentingNewLine]",
                                                                        RowBox[{"{",
                                                                                RowBox[{"pe", ",", " ",
                                                                                        RowBox[{"Quiet", "[",
                                                                                                RowBox[{"Nearest", "[",
                                                                                                        RowBox[
                                                                                                            {"goodPts",
                                                                                                             ",", "qf",
                                                                                                             ",", "1",
                                                                                                             ",",
                                                                                                             RowBox[{
                                                                                                                 "DistanceFunction",
                                                                                                                 "\[Rule]",
                                                                                                                 "toroidDist"}]}],
                                                                                                        "]"}], "]"}]}],
                                                                                "}"}]}], "]"}]}], "]"}], ";"}]}],
                                        "\[IndentingNewLine]", "]"}], ";", "\[IndentingNewLine]",
                                RowBox[{"If", "[",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{"qfn", "\[NotEqual]",
                                                        RowBox[{"{", "}"}]}], " ", "&&", " ",
                                                RowBox[{"qsn", "\[NotEqual]",
                                                        RowBox[{"{", "}"}]}], " ", "&&", " ",
                                                RowBox[{
                                                    RowBox[{"Length", "[", "edgesNNadj", "]"}], ">", "1"}]}],
                                            ",", "\[IndentingNewLine]",
                                            RowBox[{
                                                RowBox[{"qsni", " ", "=", " ",
                                                        RowBox[{
                                                            RowBox[{"Position", "[",
                                                                    RowBox[{"goodPts", ",", "qsn", ",", "1", ",", "1"}],
                                                                    "]"}], "\[LeftDoubleBracket]",
                                                            RowBox[{"1", ",", "1"}], "\[RightDoubleBracket]"}]}], ";",
                                                "\[IndentingNewLine]",
                                                RowBox[{"qfni", " ", "=", " ",
                                                        RowBox[{
                                                            RowBox[{"Position", "[",
                                                                    RowBox[{"goodPts", ",", "qfn", ",", "1", ",", "1"}],
                                                                    "]"}], "\[LeftDoubleBracket]",
                                                            RowBox[{"1", ",", "1"}], "\[RightDoubleBracket]"}]}], ";",
                                                "\[IndentingNewLine]",
                                                RowBox[{"path", " ", "=", " ",
                                                        RowBox[{"myAstar", "[",
                                                                RowBox[{
                                                                    "edgesNNadj", ",", "goodPts", ",", "qsni", ",",
                                                                    "qfni"}],
                                                                "]"}]}], ";"}]}], "\[IndentingNewLine]", "]"}], ";",
                                "\[IndentingNewLine]", "\[IndentingNewLine]",
                                RowBox[{"Graphics", "[",
                                        RowBox[{
                                            RowBox[{"{",
                                                    RowBox[{
                                                        RowBox[{"If", "[",
                                                                RowBox[{"showConfigObs", ",",
                                                                        RowBox[{"{",
                                                                                RowBox[{"Pink", ",",
                                                                                        RowBox[{"Polygon", "[", "polys",
                                                                                                "]"}]}], "}"}]}],
                                                                "]"}], ",", "\[IndentingNewLine]",
                                                        RowBox[{"toroidLines", "[",
                                                                RowBox[{"edgesNN", ",", "LightBlue", ",", "Blue"}],
                                                                "]"}],
                                                        ",", "\[IndentingNewLine]",
                                                        RowBox[{"If", "[",
                                                                RowBox[{
                                                                    RowBox[{
                                                                        RowBox[{
                                                                            RowBox[{"Length", "[", "path", "]"}],
                                                                            "\[Equal]", "0"}],
                                                                        "&&",
                                                                        RowBox[{"path", "\[Equal]",
                                                                                RowBox[{"-", "2"}]}]}], ",",
                                                                    "\[IndentingNewLine]",
                                                                    RowBox[{"{",
                                                                            RowBox[{
                                                                                RowBox[{"Thickness", "[", "0.02", "]"}],
                                                                                ",",
                                                                                RowBox[{"toroidLine", "[",
                                                                                        RowBox[{
                                                                                            RowBox[{"{",
                                                                                                    RowBox[{"qs", ",",
                                                                                                            "qf"}],
                                                                                                    "}"}], ",",
                                                                                            "Magenta"}],
                                                                                        "]"}], " ", ",",
                                                                                "\[IndentingNewLine]",
                                                                                RowBox[{
                                                                                    RowBox[{"totdist", " ", "=", " ",
                                                                                            RowBox[{"toroidDist", "[",
                                                                                                    RowBox[{"qs", ",",
                                                                                                            "qf"}],
                                                                                                    "]"}]}], ";",
                                                                                    "\[IndentingNewLine]", "Purple"}],
                                                                                ",",
                                                                                RowBox[{"PointSize", "[", "0.04", "]"}],
                                                                                ",", " ",
                                                                                RowBox[{"Point", "[",
                                                                                        RowBox[{"toroidPt", "[",
                                                                                                RowBox[{
                                                                                                    RowBox[{"{",
                                                                                                            RowBox[
                                                                                                                {"qs",
                                                                                                                 ",",
                                                                                                                 "qf"}],
                                                                                                            "}"}], ",",
                                                                                                    "progress"}],
                                                                                                "]"}], "]"}]}],
                                                                            "\[IndentingNewLine]", "}"}], ",",
                                                                    "\[IndentingNewLine]",
                                                                    RowBox[{"If", "[",
                                                                            RowBox[{
                                                                                RowBox[{
                                                                                    RowBox[
                                                                                        {"Length", "[", "path", "]"}],
                                                                                    ">", "0"}], ",",

                                                                                RowBox[{"{",
                                                                                        RowBox[{
                                                                                            RowBox[{"Thickness", "[",
                                                                                                    "0.02", "]"}], ",",
                                                                                            "\[IndentingNewLine]",
                                                                                            RowBox[{"toroidLine", "[",
                                                                                                    RowBox[{
                                                                                                        RowBox[{"{",
                                                                                                                RowBox[{
                                                                                                                    "qs",
                                                                                                                    ",",
                                                                                                                    "qsn"}],
                                                                                                                "}"}],
                                                                                                        ",",
                                                                                                        "Magenta"}],
                                                                                                    "]"}], ",",
                                                                                            "\[IndentingNewLine]",
                                                                                            RowBox[{"toroidLine", "[",
                                                                                                    RowBox[{
                                                                                                        RowBox[{"{",
                                                                                                                RowBox[{
                                                                                                                    "qf",
                                                                                                                    ",",
                                                                                                                    "qfn"}],
                                                                                                                "}"}],
                                                                                                        ",",
                                                                                                        "Magenta"}],
                                                                                                    "]"}], ",",
                                                                                            "\[IndentingNewLine]",
                                                                                            RowBox[{"Table", "[",
                                                                                                    RowBox[{
                                                                                                        RowBox[{
                                                                                                            "toroidLine",
                                                                                                            "[",
                                                                                                            RowBox[{
                                                                                                                RowBox[{
                                                                                                                    "{",
                                                                                                                    RowBox[
                                                                                                                        {
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "goodPts",
                                                                                                                                    "\[LeftDoubleBracket]",
                                                                                                                                    RowBox[
                                                                                                                                        {
                                                                                                                                            "path",
                                                                                                                                            "\[LeftDoubleBracket]",
                                                                                                                                            "i",
                                                                                                                                            "\[RightDoubleBracket]"}],
                                                                                                                                    "\[RightDoubleBracket]"}],
                                                                                                                            ",",
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "goodPts",
                                                                                                                                    "\[LeftDoubleBracket]",
                                                                                                                                    RowBox[
                                                                                                                                        {
                                                                                                                                            "path",
                                                                                                                                            "\[LeftDoubleBracket]",
                                                                                                                                            RowBox[
                                                                                                                                                {
                                                                                                                                                    "i",
                                                                                                                                                    "+",
                                                                                                                                                    "1"}],
                                                                                                                                            "\[RightDoubleBracket]"}],
                                                                                                                                    "\[RightDoubleBracket]"}]}],
                                                                                                                    "}"}],
                                                                                                                ",",
                                                                                                                RowBox[{
                                                                                                                    "Lighter",
                                                                                                                    "[",
                                                                                                                    "Green",
                                                                                                                    "]"}],
                                                                                                                ",",
                                                                                                                "Green"}],
                                                                                                            "]"}], ",",
                                                                                                        RowBox[{"{",
                                                                                                                RowBox[{
                                                                                                                    "i",
                                                                                                                    ",",
                                                                                                                    "1",
                                                                                                                    ",",
                                                                                                                    RowBox[
                                                                                                                        {
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "Length",
                                                                                                                                    "[",
                                                                                                                                    "path",
                                                                                                                                    "]"}],
                                                                                                                            "-",
                                                                                                                            "1"}]}],
                                                                                                                "}"}]}],
                                                                                                    "]"}], ",",
                                                                                            "\[IndentingNewLine]",
                                                                                            "Black", ",",
                                                                                            RowBox[{"Point", "[", "qs",
                                                                                                    "]"}], ",",
                                                                                            RowBox[{"Point", "[", "qf",
                                                                                                    "]"}], ",",
                                                                                            "\[IndentingNewLine]",
                                                                                            RowBox[{"Module", "[",
                                                                                                    RowBox[{
                                                                                                        RowBox[{"{",
                                                                                                                RowBox[{
                                                                                                                    "dists",
                                                                                                                    ",",
                                                                                                                    "c",
                                                                                                                    ",",
                                                                                                                    " ",
                                                                                                                    "distT",
                                                                                                                    ",",
                                                                                                                    RowBox[
                                                                                                                        {
                                                                                                                            "mypath",
                                                                                                                            " ",
                                                                                                                            "=",
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "Append",
                                                                                                                                    "[",
                                                                                                                                    RowBox[
                                                                                                                                        {
                                                                                                                                            RowBox[
                                                                                                                                                {
                                                                                                                                                    "Prepend",
                                                                                                                                                    "[",
                                                                                                                                                    RowBox[
                                                                                                                                                        {
                                                                                                                                                            RowBox[
                                                                                                                                                                {
                                                                                                                                                                    "goodPts",
                                                                                                                                                                    "\[LeftDoubleBracket]",
                                                                                                                                                                    "path",
                                                                                                                                                                    "\[RightDoubleBracket]"}],
                                                                                                                                                            ",",
                                                                                                                                                            "qs"}],
                                                                                                                                                    "]"}],
                                                                                                                                            ",",
                                                                                                                                            "qf"}],
                                                                                                                                    "]"}]}]}],
                                                                                                                " ",
                                                                                                                "}"}],
                                                                                                        ",", " ",
                                                                                                        RowBox[{
                                                                                                            RowBox[{
                                                                                                                "dists",
                                                                                                                " ",
                                                                                                                "=",
                                                                                                                " ",
                                                                                                                RowBox[{
                                                                                                                    "Table",
                                                                                                                    "[",
                                                                                                                    RowBox[
                                                                                                                        {
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "toroidDist",
                                                                                                                                    "[",
                                                                                                                                    RowBox[
                                                                                                                                        {
                                                                                                                                            RowBox[
                                                                                                                                                {
                                                                                                                                                    "mypath",
                                                                                                                                                    "\[LeftDoubleBracket]",
                                                                                                                                                    "i",
                                                                                                                                                    "\[RightDoubleBracket]"}],
                                                                                                                                            ",",
                                                                                                                                            RowBox[
                                                                                                                                                {
                                                                                                                                                    "mypath",
                                                                                                                                                    "\[LeftDoubleBracket]",
                                                                                                                                                    RowBox[
                                                                                                                                                        {
                                                                                                                                                            "i",
                                                                                                                                                            "+",
                                                                                                                                                            "1"}],
                                                                                                                                                    "\[RightDoubleBracket]"}]}],
                                                                                                                                    "]"}],
                                                                                                                            ",",
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "{",
                                                                                                                                    RowBox[
                                                                                                                                        {
                                                                                                                                            "i",
                                                                                                                                            ",",
                                                                                                                                            "1",
                                                                                                                                            ",",
                                                                                                                                            RowBox[
                                                                                                                                                {
                                                                                                                                                    RowBox[
                                                                                                                                                        {
                                                                                                                                                            "Length",
                                                                                                                                                            "[",
                                                                                                                                                            "mypath",
                                                                                                                                                            "]"}],
                                                                                                                                                    "-",
                                                                                                                                                    "1"}]}],
                                                                                                                                    "}"}]}],
                                                                                                                    "]"}]}],
                                                                                                            ";",
                                                                                                            "\[IndentingNewLine]",
                                                                                                            RowBox[{
                                                                                                                "totdist",
                                                                                                                " ",
                                                                                                                "=",
                                                                                                                " ",
                                                                                                                RowBox[{
                                                                                                                    "Total",
                                                                                                                    "[",
                                                                                                                    "dists",
                                                                                                                    "]"}]}],
                                                                                                            ";",
                                                                                                            "\[IndentingNewLine]",
                                                                                                            RowBox[{
                                                                                                                "distT",
                                                                                                                " ",
                                                                                                                "=",
                                                                                                                " ",
                                                                                                                "0"}],
                                                                                                            ";", " ",
                                                                                                            RowBox[{"c",
                                                                                                                    " ",
                                                                                                                    "=",
                                                                                                                    " ",
                                                                                                                    "1"}],
                                                                                                            ";", " ",
                                                                                                            RowBox[{
                                                                                                                "While",
                                                                                                                "[",
                                                                                                                RowBox[{
                                                                                                                    RowBox[
                                                                                                                        {
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "distT",
                                                                                                                                    "+",
                                                                                                                                    RowBox[
                                                                                                                                        {
                                                                                                                                            "dists",
                                                                                                                                            "\[LeftDoubleBracket]",
                                                                                                                                            "c",
                                                                                                                                            "\[RightDoubleBracket]"}]}],
                                                                                                                            "<",
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "progress",
                                                                                                                                    "*",
                                                                                                                                    "totdist"}]}],
                                                                                                                    ",",
                                                                                                                    " ",

                                                                                                                    RowBox[
                                                                                                                        {
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "distT",
                                                                                                                                    "+=",
                                                                                                                                    " ",
                                                                                                                                    RowBox[
                                                                                                                                        {
                                                                                                                                            "dists",
                                                                                                                                            "\[LeftDoubleBracket]",
                                                                                                                                            "c",
                                                                                                                                            "\[RightDoubleBracket]"}]}],
                                                                                                                            ";",
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "c",
                                                                                                                                    "++"}]}]}],
                                                                                                                "]"}],
                                                                                                            ";",
                                                                                                            "\[IndentingNewLine]",
                                                                                                            RowBox[{"{",
                                                                                                                    RowBox[
                                                                                                                        {
                                                                                                                            "Purple",
                                                                                                                            ",",
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "PointSize",
                                                                                                                                    "[",
                                                                                                                                    "0.04",
                                                                                                                                    "]"}],
                                                                                                                            ",",
                                                                                                                            " ",
                                                                                                                            RowBox[
                                                                                                                                {
                                                                                                                                    "Point",
                                                                                                                                    "[",
                                                                                                                                    RowBox[
                                                                                                                                        {
                                                                                                                                            "toroidPt",
                                                                                                                                            "[",
                                                                                                                                            RowBox[
                                                                                                                                                {
                                                                                                                                                    RowBox[
                                                                                                                                                        {
                                                                                                                                                            "{",
                                                                                                                                                            RowBox[
                                                                                                                                                                {
                                                                                                                                                                    RowBox[
                                                                                                                                                                        {
                                                                                                                                                                            "mypath",
                                                                                                                                                                            "\[LeftDoubleBracket]",
                                                                                                                                                                            "c",
                                                                                                                                                                            "\[RightDoubleBracket]"}],
                                                                                                                                                                    ",",
                                                                                                                                                                    RowBox[
                                                                                                                                                                        {
                                                                                                                                                                            "mypath",
                                                                                                                                                                            "\[LeftDoubleBracket]",
                                                                                                                                                                            RowBox[
                                                                                                                                                                                {
                                                                                                                                                                                    "c",
                                                                                                                                                                                    "+",
                                                                                                                                                                                    "1"}],
                                                                                                                                                                            "\[RightDoubleBracket]"}]}],
                                                                                                                                                            "}"}],
                                                                                                                                                    ",",
                                                                                                                                                    RowBox[
                                                                                                                                                        {
                                                                                                                                                            RowBox[
                                                                                                                                                                {
                                                                                                                                                                    "(",
                                                                                                                                                                    RowBox[
                                                                                                                                                                        {
                                                                                                                                                                            RowBox[
                                                                                                                                                                                {
                                                                                                                                                                                    "progress",
                                                                                                                                                                                    "*",
                                                                                                                                                                                    "totdist"}],
                                                                                                                                                                            "-",
                                                                                                                                                                            " ",
                                                                                                                                                                            "distT"}],
                                                                                                                                                                    ")"}],
                                                                                                                                                            "/",
                                                                                                                                                            RowBox[
                                                                                                                                                                {
                                                                                                                                                                    "dists",
                                                                                                                                                                    "\[LeftDoubleBracket]",
                                                                                                                                                                    "c",
                                                                                                                                                                    "\[RightDoubleBracket]"}]}]}],
                                                                                                                                            "]"}],
                                                                                                                                    "]"}]}],
                                                                                                                    "}"}]}]}],
                                                                                                    "]"}]}],
                                                                                        "\[IndentingNewLine]", "}"}],
                                                                                ",",
                                                                                RowBox[{"{",
                                                                                        RowBox[{
                                                                                            RowBox[{"If", "[",
                                                                                                    RowBox[{
                                                                                                        RowBox[{"qsn",
                                                                                                                "\[NotEqual]",
                                                                                                                RowBox[{
                                                                                                                    "{",
                                                                                                                    "}"}]}],
                                                                                                        ",",
                                                                                                        RowBox[{
                                                                                                            "toroidLine",
                                                                                                            "[",
                                                                                                            RowBox[{
                                                                                                                RowBox[{
                                                                                                                    "{",
                                                                                                                    RowBox[
                                                                                                                        {
                                                                                                                            "qs",
                                                                                                                            ",",
                                                                                                                            "qsn"}],
                                                                                                                    "}"}],
                                                                                                                ",",
                                                                                                                "Magenta"}],
                                                                                                            "]"}]}],
                                                                                                    "]"}], ",",
                                                                                            RowBox[{"If", "[",
                                                                                                    RowBox[{
                                                                                                        RowBox[{"qfn",
                                                                                                                "\[NotEqual]",
                                                                                                                RowBox[{
                                                                                                                    "{",
                                                                                                                    "}"}]}],
                                                                                                        ",",
                                                                                                        RowBox[{
                                                                                                            "toroidLine",
                                                                                                            "[",
                                                                                                            RowBox[{
                                                                                                                RowBox[{
                                                                                                                    "{",
                                                                                                                    RowBox[
                                                                                                                        {
                                                                                                                            "qf",
                                                                                                                            ",",
                                                                                                                            "qfn"}],
                                                                                                                    "}"}],
                                                                                                                ",",
                                                                                                                "Magenta"}],
                                                                                                            "]"}]}],
                                                                                                    "]"}]}], "}"}]}],
                                                                            " ",
                                                                            "]"}]}], "]"}], ",", "\[IndentingNewLine]",
                                                        RowBox[{"Darker", "[", "Green", "]"}], ",",
                                                        RowBox[{"PointSize", "[", "Medium", "]"}], ",",
                                                        RowBox[{"Point", "[", "goodPts", "]"}], ",", "Red", ",",
                                                        RowBox[{"Point", "[", "badPts", "]"}], ",",
                                                        "\[IndentingNewLine]",
                                                        RowBox[{"Locator", "[",
                                                                RowBox[{"qs", ",",
                                                                        RowBox[{"If", "[",
                                                                                RowBox[{
                                                                                    RowBox[{"ptInPolys", "[",
                                                                                            RowBox[
                                                                                                {"polys", ",", "qs"}],
                                                                                            "]"}], ",",
                                                                                    RowBox[{"loc", "[", "Red", "]"}],
                                                                                    ",",
                                                                                    RowBox[{"loc", "[",
                                                                                            RowBox[
                                                                                                {"Darker", "[", "Green",
                                                                                                 "]"}], "]"}]}],
                                                                                "]"}]}], "]"}], ",",
                                                        "\[IndentingNewLine]",
                                                        RowBox[{"Locator", "[",
                                                                RowBox[{"qf", ",",
                                                                        RowBox[{"If", "[",
                                                                                RowBox[{
                                                                                    RowBox[{"ptInPolys", "[",
                                                                                            RowBox[
                                                                                                {"polys", ",", "qf"}],
                                                                                            "]"}], ",",
                                                                                    RowBox[{"loc", "[", "Red", "]"}],
                                                                                    ",",
                                                                                    RowBox[{"loc", "[",
                                                                                            RowBox[
                                                                                                {"Darker", "[", "Green",
                                                                                                 "]"}], "]"}]}],
                                                                                "]"}]}], "]"}]}], "\[IndentingNewLine]",
                                                    "\[IndentingNewLine]", "}"}], ",",
                                            RowBox[{"PlotLabel", " ", "\[Rule]", " ",
                                                    RowBox[{"If", "[",
                                                            RowBox[{
                                                                RowBox[{
                                                                    RowBox[{
                                                                        RowBox[{"Length", "[", "path", "]"}],
                                                                        "\[Equal]", "0"}],
                                                                    "&&",
                                                                    RowBox[{"path", "\[Equal]",
                                                                            RowBox[{"-", "1"}]}]}], ",",
                                                                "\"\<no path possible\>\"",
                                                                ",",
                                                                RowBox[{"StringForm", "[",
                                                                        RowBox[{"\"\<path length = ``\>\"", ",",
                                                                                RowBox[{"Round", "[",
                                                                                        RowBox[{"totdist", ",", ".01"}],
                                                                                        "]"}]}], "]"}]}],
                                                            "]"}]}], ",", "\[IndentingNewLine]",
                                            RowBox[{"Axes", "\[Rule]", "True"}], ",",
                                            RowBox[{"AxesOrigin", "\[Rule]",
                                                    RowBox[{"{",
                                                            RowBox[{"0", ",", "0"}], "}"}]}], ",",
                                            RowBox[{"PlotRange", "\[Rule]",
                                                    RowBox[{"{",
                                                            RowBox[{
                                                                RowBox[{"{",
                                                                        RowBox[{"0", ",",
                                                                                RowBox[{"2", "\[Pi]"}]}], "}"}], ",",
                                                                RowBox[{"{",
                                                                        RowBox[{"0", ",",
                                                                                RowBox[{"2", "\[Pi]"}]}], "}"}]}],
                                                            "}"}]}]}], "]"}]}]}],
                        "]"}], ",", "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"qf", ",",
                                            RowBox[{"{",
                                                    RowBox[{"5", ",", "5"}], "}"}]}], "}"}], ",",
                            RowBox[{"{",
                                    RowBox[{
                                        RowBox[{"-", ".1"}], ",",
                                        RowBox[{"-", ".1"}]}], "}"}], ",",
                            RowBox[{"{",
                                    RowBox[{
                                        RowBox[{"2.1", "\[Pi]"}], ",",
                                        RowBox[{"2.1", "\[Pi]"}]}], "}"}], ",", "Locator", ",",
                            RowBox[{"Appearance", "\[Rule]", "None"}]}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"qs", ",",
                                            RowBox[{"{",
                                                    RowBox[{"1", ",", "1"}], "}"}]}], "}"}], ",",
                            RowBox[{"{",
                                    RowBox[{
                                        RowBox[{"-", ".1"}], ",",
                                        RowBox[{"-", ".1"}]}], "}"}], ",",
                            RowBox[{"{",
                                    RowBox[{
                                        RowBox[{"2.1", "\[Pi]"}], ",",
                                        RowBox[{"2.1", "\[Pi]"}]}], "}"}], ",", "Locator", ",",
                            RowBox[{"Appearance", "\[Rule]", "None"}]}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"pts", ",",
                                            RowBox[{"{", "}"}]}], "}"}], ",", "None"}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"addPoints", ",", "False"}], "}"}], ",", "None"}],
                        "}"}], ",", "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"restart", ",", "True"}], "}"}], ",", "None"}], "}"}],
                ",", "\[IndentingNewLine]",
                RowBox[{"Button", "[",
                        RowBox[{"\"\<add 50 vertices\>\"", ",",
                                RowBox[{"addPoints", "=", "True"}], ",",
                                RowBox[{"ImageSize", "\[Rule]", "140"}]}], "]"}], ",",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"r", ",", "0.5", ",", "\"\<radius\>\""}], "}"}], ",",
                            "0", ",", "1", ",", "0.01", ",",
                            RowBox[{"Appearance", "\[Rule]", "\"\<Labeled\>\""}], ",",
                            RowBox[{"ImageSize", "\[Rule]", "100"}]}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{"progress", ",", "0", ",", "1", ",", "0.01", ",",
                                RowBox[{"Enabled", "\[Rule]",
                                        RowBox[{
                                            RowBox[{
                                                RowBox[{"Length", "[", "path", "]"}], ">", "0"}], "||",
                                            RowBox[{"path", "\[Equal]",
                                                    RowBox[{"-", "2"}]}]}]}], ",",
                                RowBox[{"Appearance", "\[Rule]", " ", "\"\<Labeled\>\""}], ",",
                                RowBox[{"ImageSize", "\[Rule]", "100"}]}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{
                                        "showConfigObs", ",", "False", ",", "\"\<show obstacles\>\""}],
                                    "}"}], ",",
                            RowBox[{"{",
                                    RowBox[{"False", ",", "True"}], "}"}]}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"Button", "[",
                        RowBox[{"\"\<restart\>\"", ",",
                                RowBox[{"restart", "=", "True"}], ",",
                                RowBox[{"ImageSize", "\[Rule]", "140"}]}], "]"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"path", ",",
                                            RowBox[{"-", "1"}]}], "}"}], ",", "None"}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"rold", ",",
                                            RowBox[{"-", "1"}]}], "}"}], ",", "None"}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"badPts", ",",
                                            RowBox[{"{", "}"}]}], "}"}], ",", "None"}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"goodPts", ",",
                                            RowBox[{"{", "}"}]}], "}"}], ",", "None"}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"edgesNN", ",",
                                            RowBox[{"{", "}"}]}], "}"}], ",", "None"}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"edgesNNadj", ",",
                                            RowBox[{"{", "}"}]}], "}"}], ",", "None"}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"polyN", " ", ",", "4"}], "}"}], ",", "None"}], "}"}],
                ",", "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"polySides", " ", ",",
                                            RowBox[{"{", "}"}]}], "}"}], ",", "None"}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"polys", " ", ",",
                                            RowBox[{"{", "}"}]}], "}"}], ",", "None"}], "}"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"{",
                        RowBox[{
                            RowBox[{"{",
                                    RowBox[{"polyXY", " ", ",",
                                            RowBox[{"{", "}"}]}], "}"}], ",", "None"}], "}"}], ",",
                RowBox[{"ControlPlacement", "\[Rule]", "Left"}], ",",
                "\[IndentingNewLine]",
                RowBox[{"SaveDefinitions", "\[Rule]", "True"}]}],
            "\[IndentingNewLine]", "]"}]], "Input",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
CellChangeTimes->{{3.782497440137124 * ^ 9, 3.7824975639811077` * ^ 9}, {
    3.78249764901925 * ^ 9, 3.7824978662393627` * ^ 9}, {
                      3.782497995915628 * ^ 9, 3.782498099124723 * ^ 9}, {3.782498151369108 * ^ 9,
                                                                          3.782498216522767 * ^ 9},
                  {3.78249829583267 * ^ 9,
                   3.782498301444407 * ^ 9}, {3.782498332720305 * ^ 9,
                                              3.782498372705511 * ^ 9}, {3.782498472431055 * ^ 9,
                                                                         3.782498580154088 * ^ 9}, {3.7824986827342043
                  ` * ^ 9,
                  3.782498700681727 * ^ 9}, {3.782498761392468 * ^ 9,
                                             3.782498851843178 * ^ 9}, {3.7824990384575653
` * ^ 9,
3.782499088378078 * ^ 9}, {3.782499146638846 * ^ 9,
                           3.782499206593154 * ^ 9}, {3.782500307121359 * ^ 9,
                                                      3.782500330752532 * ^ 9}, {3.782500368190407 * ^ 9,
                                                                                 3.782500481174713 * ^ 9}, {
    3.7825005409047623
` * ^ 9,
3.7825006582155247
` * ^ 9}, {3.782500936357027 * ^ 9,
           3.7825009615653687` * ^ 9}, {3.782512819685872 * ^ 9,
                                        3.782512822210376 * ^ 9}, {3.7825129488874702
` * ^ 9,
3.7825130023710203
` * ^ 9}, {3.782513037663007 * ^ 9,
           3.782513196695211 * ^ 9}, 3.78251325543364 * ^ 9, {
    3.7825132874221363
` * ^ 9, 3.782513299005913 * ^ 9}, {
    3.78251337896903 * ^ 9, 3.782513380026617 * ^ 9}, {3.782513419740696 * ^ 9,
                                                       3.7825134375302267` * ^ 9}, {3.782513546353159 * ^ 9,
                                                                                    3.7825135486067257` * ^ 9}, {
    3.782513592555175 * ^ 9,
    3.782513732892919 * ^ 9}, {3.782513774858745 * ^ 9,
                               3.782513798914163 * ^ 9}, {3.782513947902426 * ^ 9,
                                                          3.782513980699069 * ^ 9}, 3.782514030206902 * ^ 9, {
    3.782514097391892 * ^ 9,
    3.782514200441128 * ^ 9}, {3.7825142615361233
` * ^ 9,
3.7825142855514317
` * ^ 9}, 3.782514326418167 * ^ 9, {
    3.782514449775069 * ^ 9, 3.7825144836135807` * ^ 9}, {
    3.7825145714867163
` * ^ 9, 3.782514606660995 * ^ 9}, {
    3.782519537093659 * ^ 9, 3.782519547753182 * ^ 9}, {3.78251962006334 * ^ 9,
                                                        3.782519651503107 * ^ 9}, {3.78257375265985 * ^ 9,
                                                                                   3.782573916400446 * ^ 9}, {
    3.782573958369534 * ^ 9,
    3.782573981836039 * ^ 9}, {3.782574021634864 * ^ 9,
                               3.7825740230602407` * ^ 9}, {3.7825740573378887
` * ^ 9,
3.782574138167053 * ^ 9}, {3.7825741742559 * ^ 9,
                           3.7825742865576963` * ^ 9}, {3.782574760066864 * ^ 9,
                                                        3.78257481794265 * ^ 9}, {3.78260134481805 * ^ 9,
                                                                                  3.782601345117814 * ^ 9}, {
    3.7826015599155684
` * ^ 9,
3.782601637179913 * ^ 9}, {3.782601825986812 * ^ 9,
                           3.782601826933393 * ^ 9}, {3.783120446322063 * ^ 9,
                                                      3.783120464138913 * ^ 9}, {3.783120524273448 * ^ 9,
                                                                                 3.7831206884620934` * ^ 9}, {
    3.783120914438216 * ^ 9,
    3.783120985611331 * ^ 9}, 3.783121017469549 * ^ 9, {3.783121082551276 * ^ 9,
                                                        3.7831212223238897` * ^ 9}, {3.78317698243194 * ^ 9,
                                                                                     3.7831770275717163` * ^ 9}, {
    3.7831770978949013
` * ^ 9,
3.783177117717334 * ^ 9}, {3.783177177277368 * ^ 9,
                           3.783177231887044 * ^ 9}, {3.783177301562224 * ^ 9,
                                                      3.783177466939502 * ^ 9}, {3.783177540468377 * ^ 9,
                                                                                 3.783177609348905 * ^ 9}, {
    3.783177680317931 * ^ 9,
    3.78317770102777 * ^ 9}, {3.783177747209271 * ^ 9,
                              3.7831777692153187` * ^ 9}, {3.7831778032839403
` * ^ 9,
3.7831778100462418
` * ^ 9}, 3.7831778932429543
` * ^ 9, {
    3.783179111493846 * ^ 9, 3.783179118161693 * ^ 9},
3.783179158627776 * ^ 9, {3.783179230916113 * ^ 9,
                          3.783179273291617 * ^ 9}, {3.783179342787401 * ^ 9,
                                                     3.783179386646454 * ^ 9}, {3.7831794599509077
` * ^ 9,
3.7831796432072144
` * ^ 9}, {3.7831797339481792
` * ^ 9,
3.783179737723773 * ^ 9}, {3.78317978433391 * ^ 9,
                           3.783179888146118 * ^ 9}, {3.7834177697526817
` * ^ 9,
3.783417795087042 * ^ 9}, {3.783431867923061 * ^ 9,
                           3.783431917774411 * ^ 9}, {3.783431961180624 * ^ 9,
                                                      3.7834319901055813` * ^ 9}, {3.78344977145366 * ^ 9,
                                                                                   3.7834498456432743` * ^ 9}, {
    3.7834501199684277
` * ^ 9,
3.783450157537499 * ^ 9}, {3.783450334111537 * ^ 9,
                           3.783450358584968 * ^ 9}, {3.7834504363026323
` * ^ 9,
3.783450437744339 * ^ 9}, {3.783450490558276 * ^ 9, 3.78345057285077 * ^ 9},
3.783450651048238 * ^ 9, {3.7834531328022213
` * ^ 9,
3.7834532202161827
` * ^ 9}, {3.783453262510746 * ^ 9,
           3.78345343995901 * ^ 9}, {3.783453479994134 * ^ 9,
                                     3.783453535437833 * ^ 9}, {3.783453580798675 * ^ 9,
                                                                3.783453798828595 * ^ 9}, {3.783454046500284 * ^ 9,
                                                                                           3.78345432380149 * ^ 9}, {
    3.7834543931372128
` * ^ 9,
3.783454512410561 * ^ 9}, {3.783454561834466 * ^ 9,
                           3.7834545697580023` * ^ 9}, {3.783454603824718 * ^ 9,
                                                        3.783454623151472 * ^ 9}, {3.783454735509778 * ^ 9,
                                                                                   3.783454737233185 * ^ 9}, {
    3.78345483529583 * ^ 9,
    3.783454844444275 * ^ 9}, {3.783454907806271 * ^ 9,
                               3.7834549300628242` * ^ 9}, {3.783454987173601 * ^ 9,
                                                            3.7834550155786324` * ^ 9}, {3.7834550983314257
` * ^ 9,
3.783455113038855 * ^ 9}, {3.783458394811289 * ^ 9,
                           3.783458396890181 * ^ 9}, {3.783458465558755 * ^ 9,
                                                      3.7834584821217613` * ^ 9}, 3.783458668142642 * ^ 9, {
    3.7834588523259706
` * ^ 9, 3.78345885407168 * ^ 9}, {
    3.7834588856056213
` * ^ 9, 3.783458952552491 * ^ 9}, {
    3.783459027193761 * ^ 9, 3.783459057033367 * ^ 9}, {3.783459099278977 * ^ 9,
                                                        3.783459142421283 * ^ 9}, {3.783459208785902 * ^ 9,
                                                                                   3.7834592384270353` * ^ 9}, {
    3.783459811558763 * ^ 9,
    3.783459888112989 * ^ 9}, {3.7834599576462927
` * ^ 9,
3.783459960536935 * ^ 9}, 3.783460241501717 * ^ 9, {3.783460300973783 * ^ 9,
                                                    3.7834604881009073` * ^ 9}, {3.783460547222989 * ^ 9,
                                                                                 3.7834605886194687` * ^ 9}, {
    3.783460644726988 * ^ 9,
    3.783460719794549 * ^ 9}, 3.783460805101191 * ^ 9, {3.7834608387494 * ^ 9,
                                                        3.783460970916551 * ^ 9}, {3.7834610745441637
` * ^ 9,
3.783461074845791 * ^ 9}, {3.783461116980454 * ^ 9,
                           3.7834611620877943` * ^ 9}, {3.783461207342046 * ^ 9,
                                                        3.783461214325096 * ^ 9}, {3.783461276555983 * ^ 9,
                                                                                   3.783461276900983 * ^ 9}, {
    3.7834613448602667
` * ^ 9,
3.783461411058936 * ^ 9}, {3.783461458053217 * ^ 9,
                           3.783461461807868 * ^ 9}, {3.783461523506051 * ^ 9,
                                                      3.7834615829750357` * ^ 9}, {3.78346164004775 * ^ 9,
                                                                                   3.78346164394843 * ^ 9}, {
    3.783461696001265 * ^ 9,
    3.783461706583297 * ^ 9}, {3.783461910562615 * ^ 9,
                               3.783461923382517 * ^ 9}, 3.78346209398956 * ^ 9, {3.783462187173864 * ^ 9,
                                                                                  3.783462188672441 * ^ 9}, 3.7834633795855494
` * ^ 9, {
    3.783463667428967 * ^ 9, 3.783463667745598 * ^ 9}, {3.783465329401251 * ^ 9,
                                                        3.7834653373774223` * ^ 9}, 3.7834653756473017
` * ^ 9,
3.7834665807544117
` * ^ 9, {3.7834669024234543
` * ^ 9,
3.783466916200156 * ^ 9}, {3.783467154205146 * ^ 9,
                           3.7834672196215973` * ^ 9}, {3.783467263819304 * ^ 9,
                                                        3.78346726430284 * ^ 9}, 3.783467459743602 * ^ 9, 3.783467494630847 * ^ 9, {
    3.7836194318695803
` * ^ 9, 3.783619457194824 * ^ 9}, {
    3.7836195445113697
` * ^ 9, 3.783619613928174 * ^ 9}, {
    3.783625574507978 * ^ 9, 3.783625706367991 * ^ 9}, {3.783625754452039 * ^ 9,
                                                        3.783625791922928 * ^ 9}, {3.7836258312302094
` * ^ 9,
3.783625934892308 * ^ 9}, {3.7836259650588093
` * ^ 9,
3.783625971189375 * ^ 9}, {3.783626012131481 * ^ 9,
                           3.783626087264268 * ^ 9}, {3.783626136761694 * ^ 9,
                                                      3.7836261784138527` * ^ 9}, {3.783626216853403 * ^ 9,
                                                                                   3.7836262192333317` * ^ 9}, {
    3.783626289595042 * ^ 9,
    3.783626307104233 * ^ 9}, {3.783626342937214 * ^ 9,
                               3.783626386994067 * ^ 9}, {3.783626482509704 * ^ 9,
                                                          3.78362650952691 * ^ 9}, {3.783626554375656 * ^ 9,
                                                                                    3.7836265602854967` * ^ 9}, {
    3.7836265912783613
` * ^ 9,
3.783626685072854 * ^ 9}, {3.783626744579431 * ^ 9,
                           3.783626751084058 * ^ 9}, {3.7836268436197433
` * ^ 9,
3.783626889518148 * ^ 9}, {3.7836269196091423
` * ^ 9,
3.783626922588861 * ^ 9}, {3.7836269845807037
` * ^ 9,
3.783627014773994 * ^ 9}, {3.783627062839059 * ^ 9,
                           3.783627131893262 * ^ 9}, {3.783627247798377 * ^ 9,
                                                      3.783627253995717 * ^ 9}, {3.783627305340372 * ^ 9,
                                                                                 3.783627307596817 * ^ 9}, {
    3.783627394649251 * ^ 9,
    3.7836274059789886` * ^ 9}, {3.78362748034403 * ^ 9,
                                 3.783627495107307 * ^ 9}, {3.783628193247034 * ^ 9,
                                                            3.783628195367989 * ^ 9}, {3.783632549260695 * ^ 9,
                                                                                       3.783632563958171 * ^ 9}, {
    3.783632659053049 * ^ 9,
    3.7836326846380367` * ^ 9}, {3.783632756069376 * ^ 9,
                                 3.783632777012252 * ^ 9}, {3.783632822755645 * ^ 9,
                                                            3.783632862256884 * ^ 9}, {3.783633208200693 * ^ 9,
                                                                                       3.783633291016898 * ^ 9}, {
    3.783633358340332 * ^ 9,
    3.783633370281267 * ^ 9}, {3.783634195301859 * ^ 9,
                               3.783634272713382 * ^ 9}, 3.783634511015234 * ^ 9, {3.783634579143649 * ^ 9,
                                                                                   3.783634617185627 * ^ 9}, {
    3.783634651142734 * ^ 9,
    3.783634659600058 * ^ 9}, {3.783635128480316 * ^ 9,
                               3.783635255995298 * ^ 9}, {3.783635293716364 * ^ 9,
                                                          3.783635421865086 * ^ 9}, {3.783635491407124 * ^ 9,
                                                                                     3.7836358634581327` * ^ 9}, {
    3.783635917491049 * ^ 9,
    3.783635943791946 * ^ 9}, {3.7836396840148697
` * ^ 9,
3.783639752177473 * ^ 9}, 3.783639851725109 * ^ 9, {3.783639928660878 * ^ 9,
                                                    3.783639929971828 * ^ 9}, 3.7836400589640827
` * ^ 9, {
    3.783640101842146 * ^ 9, 3.7836401320381804` * ^ 9}, {
    3.7836401876613407
` * ^ 9, 3.783640198354772 * ^ 9}, {
    3.7836402815762043
` * ^ 9, 3.7836403404810667
` * ^ 9}, {
    3.7836404083524513
` * ^ 9, 3.783640413155834 * ^ 9}, {
    3.783640498143671 * ^ 9, 3.7836405017100677` * ^ 9}, {
    3.783640567526408 * ^ 9, 3.7836405741767597` * ^ 9}, {
    3.783640606408415 * ^ 9, 3.783640619808919 * ^ 9}, {
    3.7836407644648533
` * ^ 9, 3.783640788493107 * ^ 9}, {
    3.783640832637783 * ^ 9, 3.783640843328166 * ^ 9}, {3.783640891521138 * ^ 9,
                                                        3.783640938527378 * ^ 9}, 3.7836410295582857
` * ^ 9, {
    3.783642536624978 * ^ 9, 3.783642584233317 * ^ 9},
3.7836426542626247
` * ^ 9, {3.783642756772572 * ^ 9,
          3.7836427971275053` * ^ 9}, {3.783642837312756 * ^ 9,
                                       3.783642872548479 * ^ 9}, {3.783642918154459 * ^ 9,
                                                                  3.783642925511251 * ^ 9}, {3.783642999508541 * ^ 9,
                                                                                             3.7836431075186787
                                                                                             ` * ^ 9}, {
    3.783643163178452 * ^ 9,
    3.783643195801284 * ^ 9}, {3.78364327679177 * ^ 9,
                               3.783643313206812 * ^ 9}, {3.783643944828617 * ^ 9,
                                                          3.783643946279503 * ^ 9}, {3.783644003713337 * ^ 9,
                                                                                     3.7836440476912603` * ^ 9}, {
    3.78367639861821 * ^ 9,
    3.783676581965147 * ^ 9}, {3.783676635148128 * ^ 9,
                               3.7836766858872337` * ^ 9}, 3.7836767308045692
` * ^ 9, {
    3.783679615280919 * ^ 9, 3.783679623758739 * ^ 9}, {
    3.7837008597201147
` * ^ 9, 3.78370086993163 * ^ 9}, {
    3.783705096630496 * ^ 9, 3.783705097690943 * ^ 9}, {3.78370512871717 * ^ 9,
                                                        3.783705137728169 * ^ 9}, {3.7837051712196207
` * ^ 9,
3.7837051843509617
` * ^ 9}, {3.7837052364903316
` * ^ 9,
3.7837052403019447
` * ^ 9}, {3.783729250087717 * ^ 9,
           3.783729251196102 * ^ 9}, {3.783729921195821 * ^ 9,
                                      3.783729922945207 * ^ 9}, {3.7837303350074472
` * ^ 9,
3.783730358340517 * ^ 9}, {3.7837303977569933
` * ^ 9,
3.7837304972290573
` * ^ 9}, {3.784576605299493 * ^ 9,
           3.784576606906473 * ^ 9}, {3.78569330181931 * ^ 9,
                                      3.785693363930814 * ^ 9}, {3.7856934202629128
` * ^ 9,
3.785693496443221 * ^ 9}, {3.785693585812112 * ^ 9,
                           3.785693608156691 * ^ 9}, {3.785693914731861 * ^ 9,
                                                      3.785694037369771 * ^ 9}, {3.7856942604166937
` * ^ 9,
3.785694260745966 * ^ 9}, {3.785694396235652 * ^ 9,
                           3.785694406548079 * ^ 9}, {3.785694868848248 * ^ 9,
                                                      3.785694871623852 * ^ 9}, {3.785694917712596 * ^ 9,
                                                                                 3.785694918249379 * ^ 9}, {
    3.785694993474267 * ^ 9,
    3.7856950417666197` * ^ 9}, {3.785695073980764 * ^ 9,
                                 3.785695114843045 * ^ 9}, {3.7856951722394323
` * ^ 9,
3.785695180654109 * ^ 9}, {3.785695211074881 * ^ 9,
                           3.7856952118016157` * ^ 9}, 3.785695335755828 * ^ 9, {
    3.785695374238948 * ^ 9, 3.7856953768718653` * ^ 9}, {
    3.785695540447692 * ^ 9, 3.785695555236504 * ^ 9}, {3.785695608958008 * ^ 9,
                                                        3.785695609109098 * ^ 9}, {3.7856958736837673
` * ^ 9,
3.7856958835158453
` * ^ 9}, {3.785695937649857 * ^ 9,
           3.7856959528895903` * ^ 9}, {3.7856960962498713
` * ^ 9,
3.785696099350919 * ^ 9}, {3.785859371805347 * ^ 9,
                           3.785859372234833 * ^ 9}, {3.7858594195292664
` * ^ 9,
3.7858594552804337
` * ^ 9}, {3.785859845536186 * ^ 9,
           3.785859888058152 * ^ 9}, {3.785861051486052 * ^ 9,
                                      3.7858610526711273` * ^ 9}, {3.785861103248225 * ^ 9,
                                                                   3.785861104244831 * ^ 9}, {3.7858611549719067
` * ^ 9,
3.785861157004476 * ^ 9}, {3.78586119447771 * ^ 9,
                           3.7858611962564917` * ^ 9}, {3.785861339571232 * ^ 9,
                                                        3.7858614151721563` * ^ 9}, {3.785873299528215 * ^ 9,
                                                                                     3.785873322848205 * ^ 9}, {
    3.78701363198974 * ^ 9,
    3.787013648501405 * ^ 9}, {3.787013701262574 * ^ 9,
                               3.787013837367835 * ^ 9}, {3.787062723717108 * ^ 9,
                                                          3.787062781586136 * ^ 9}, {3.7870628126802692
` * ^ 9,
3.787062820510047 * ^ 9}, {3.787062868827825 * ^ 9,
                           3.787062885453682 * ^ 9}, {3.7870633162441483
` * ^ 9,
3.787063327356613 * ^ 9}, {3.787063389784466 * ^ 9,
                           3.787063411866665 * ^ 9}, 3.787064569234931 * ^ 9, 3.788641593869793 * ^ 9},

CellID->1784167963],

Cell[BoxData[
    TagBox[
        StyleBox[
            DynamicModuleBox[{$CellContext
`addPoints$$ =
False, $CellContext
`badPts$$ = CompressedData["
1: eJwVVH041AkXHdMorEHNx2 + y6dsmjdKmpXzcu3rakCK072xpKxttSoblbapR
bXkzSbKahqSyIm1q0MqSopZKUUZmw0uMfORzMDP8Zkbszv5xn / PPfZ5z7nnO
PYtCIgNCqRQK5ZBh / kW79Zq6sN1dMCTvKv96WAvBIh4tRcjC7Naezs4TBFpc
2
OW8PZHARGtaWDuykfnD2Pkdi80xpdo3dNn1bnDcbDEk3jsMT1pPrmuLHgZe
SdwSYe8omG874b3e1wgViheHecZqKIz7yzSyzLB3M6JcSyNQnsi + 8
yiDwLvx
fFHjAxbWyUriHuuZeCfoDqlzZ2N06bOHuTIO8mkf33f4sXG6RtGhfsdC5pRl
7
NMZE + AmoYU6 / ELFNtFmcnghEx1LvYUZpzuhpuHbBcxmNWTxyRZ9gBJqdvV1
dlXoYeib5VGLwylYWPVynmYbA71aNMq4jAEoTm7eSvzNwCxOpWR6HQddsqon
k2yMUesm3dRRPwwpA2Zn6RF0FHwRx42qHYRia4 + QvCJjdCmg8S6 / 1
IBgbayu
toQEEa0kz4xUAU8o0NVoWShgPdnQ8VQJOX6zpP2vzZFSMREn8xgDTY1whrda
BZoHF1dKQmdg3ar2axlfmqNLuyRzucs0FO + v3GWeRUNFjyK4LV4JxXUj7gP6
MUgvmmPkaWyE / jfCVh / 7
OAncshK / tSQFXylik + MpbMy6SbMj + RpwGmg8RT0w
CoWBY49PDU6DvHqxmiM1RVlDFD24eAhkeG5RUPEkxBw + sjX7kxoSW + yd87IZ
KOeZystms / H5o6HCq4EEFq446 / 5u
1
gfIdCxYmr2ZgW8PnLqf2sxGnwMnHxd9
RSBlib34 + 74
xKCWFO42MjLE5hy + 7U
DAE / musbv + vawRQefzwzdkTIEtIaNTd
n4KcnPYtHFc9JF21Oxp12RSXxobt37h / FIrpfU // LDDFLNvKZnlSP3iJzm44
f5OG6TMlH + WWhnt6Xq00f0CgqLCq / JLdB7CPvWu1aS6BvEyb / 17 / YwhShIKN
56
wMfGdqxRFpKoi / 5
pn4WjwLu98ElymfasDx1Zm1VVkW2Kxj733EU0M1Mo //
mm2G834J8JdqxqGtitVW0cVCx4bTvt0xGpB / ZnYyKZ2Ool / fxhDXJsGtTOK5
P4wEWkfQ9r3jVOQGiiMKQtkY38FsmrlRDV4cm2bd + r8hs1L1BfWIGlzqb + de
OtID1c5bzx + kGGFK8sYVz25YYl + 1
ie3OV1rodnOqD2 / Qg1vU3kabJVSU33Jz
nzubjkicj / 9
cbNAjPR71LI2BnOzDHZtdCOy28thhE0LDhX6KJa7VOihUL0ij
RRqjvKuy7DJ1EuKdAym7N6khx8sMAyZJeBjH / H / RaRZ6CYJDZniQ8OGK / JD9
aibK5q5fqb9FoMA1VbSFTQLW39u8s1EJbXW1reauFDTZImhpLxyHUkH9dy6X
pqGNvzh / jCBhz9RMiZsPA + 1
kk / sGbEfAavry8lwVE98d5ZNkAhuFPs / 2
PXlB
RxfK63sPkrUgf1ZltNFHBYq7KsmGKT2M9laes / 79
I3jNDjDhHqPgp9qfuVU /
W6BcET7eNDgK2qQ8aeRLEyxdk // j0JUeSKSbrebMYhp8qz4R5UZgsBgVB0eY
OO + e1KLcaRJqMsiQmD + 0
wHf05r5Wk6A17RfnZFjg0PCejABSC5n7euO76Gys
2
GDvpzjEQY + tDx0WeLPRrYY358XvBPb57JnvH87GpDGx3bkyNfCdtDc + +1
MJ
bsOpF8tLDX0yuPC37F10nJcoVvgmjIJvWuRzz5gZGER81fnYwZD3KOu1DhdU
4
P + fbklTuB4W57fqGV4Ehh9bVmuRzkb8UurM6KWjU39udHn + BIi / Dpo / 5
WiB
ezw47yi5I / Apqyd0WxyBKaRnSyy3G + xWTAzdP2Nq6Dly3HhiEoQbpEqZRAUp
lrdUnTlUFCquv1121JC3K6Kfoi + MQrytbZOJtyUWBlZYrHQaB + pPNveNR + cg
Zd4dUWptNzx6dTYjfcUocD8PbttxlYRvSK9V2t1slPxAfdPtyULPlC5uc / Qc
lC1MbV3V2A / 8
OpPrmgYGLnQPaUqNUMH6m5uiU6JZ2MarTEiu1AHNL6vF6eC /
/ wOCJ9wREPF81pTI6OjfTwvxcSDhxMvXrj6uLLQqqpDuMtKBwuG3 / GLdAJhf
rXe6TlCw + b0kr9faGDnHnepc0kbgOaFctciVgUsH / S8KQ8ZgpbvC8r4vC + O /
k7yfrx6H9Ikt5VUJfdA3HWMUWzcFP8YUXfvWzxzT1yVXp93 + AHXHGAg6g7 / b
86
y932jhHxG0PWo =
"], $CellContext`edgesNN$$ = CompressedData["
1: eJyF3Xlczen7 + PHTon077ciI8aHBUHZNvG / JbixhZM8yZBllzyChQdaMEEII
ISZ7Y0mWsU9iQkMpCtkSJaHM73wfv / 9e1
zwe88f3j / k + P + c4nfN + 3 / d1Xfd1
3 + 86
o0IDfzTR6XQ3zHQ6Y93 // z + vrvdfbthlrW4njdkQ + thdBTW4WaQKbJTu
SHDgwK + 3
avSkdWO1Aa0tVcZZ25XTKtwV3Wb / o3ljJ9mppTX / cL5iL33uFqOr
bc9YKE / P953H2WaI94 / ssX / r / Kl2qvtvKy8YhbuJ18eO9Oxu0t5a9Wn7v8X3
rHLE6zNr / dN3xXsbFZfV1 / nJfVfx + sRj / eb0Pm6vks6N6jvwa / n5vD + l5hb0
NVeprRwuDraWvmN6qWNKYwd1 / 8 / vGp8 + 46
aCJp7pvT7gHy3lXPkf5 + a7qaL4
XenjXL5oNbYmHW + bL / 3
Kx6KbpxZ / 1
pJejTS1fesqfG7w + sqrCZ + 0
rrU9XF + 7
uQtPTj9Yf / Z1Y9Xm6iL3nCXy / b22HNjzvxsV2skPufYjEqVH + u6eYpllrNS2
AVFPiv7FUws / 7
P3wWdNtXKp71eaARve8 / KAsr4OxemG0pPvgEhfx + rCI8rwJ
jT5pAUEuwT8cll540Cu6ZnS5dq3zvjtn3A3f9 / Rn5fdXF2qmJsufrnzmrtR6
F3 / bO3e0yteRE4fOlx5 + Obbv1eRHmuOjG4t / OOAmvM3C41aVo99qCe8mGC / o
9
odGTz9bvmjbmBQt8kyLLnX9koSH / LZjTmKPMs31w83Y0K3y3 / +vzx9 / N3d9
9
ZalWkiNguykgnwt / 82l
Qp + b6Zpvz / CdSzu5qLTXA9W9HMP / buNAyx2lzoru
nnz7uP8ed3Xjl + iap6 + 7
CE8wdoyYFHpeC8xe + Tmlxr + 8 / ptjvduPfawFDLwb
XnOQfH16zLFnG65c1cIONB9xb76TcF3y7dnL8vZpZU7htdd2lZ5vlf65MLpQ
K9zaJyNDyfcPrhboYfTZTTU02nyq1j1X + frjAcMarLuo9fG9 / GHQTUfhYfbe
GVUtcjS / 3
zfGxJ1wVBeH7An0 / c5UTZrc4sHa4 + 7
i + qXz / hC + s8088xWmalTe
VPfPdaXz / qdHnfYd7jmgmkopuurrVEO + 3u
J / H2YsbldN7TjRy7tRqqvw6W8P
rXljbqZSGjabvnf1PY0e9Pl / O1svMla6h / nr4zf + LZzjr3g97rfO / UOdHfa7
qibTVl98uM5Z6X70G1OyxFU1y + 5
y60CEs / CIuJPGzy64qq0ral4uzXQSPnjR
4
EM + Qa6qa0PPQWFTpdtNGTqnysZVxcwZW7r1nKPw2KRn5SuPOKvJi2uk1C + T
r + f9Qe9cPvyu3sxVHb7frV / GcPn + / l92t28 / yk2ldLe + N3 + odLP1Z3vf6Oys
jJ91 / fHnP5yUiv5Bn1i3StPpW + 6
YduyO1nXNGp / Tv1RqKTu2hufseaDROT7S
L67J + rvf7A9a8Ig5nR / 1u
C3cxv / k4dveRiok66vKBJMnwousgs406VilpaZl
FJ8vfy6c1wc96crLnqVfGSuvc8l1G3UtEJ74zGdTjabGKmFe6ra + SwqFc / 6
h
D9VFt25eUKrFOM6 + dCyjQBub69Tc3tFFJXWp6H3Lw1Sl12v19 / 5
bziplgdnf
UzxMFN24od9c4xYuqjBk + oxTs6oJd3ex6 / nPX84q23LYuPNbpV / LCAieM95Z
ma69X6vSTvqoixenDihwUVH2K1 + sc5U + uePyqtkWrip14IQHW5 + bCr90o9fO
YT6uKiHHbEDDUPn6stOpIxY0NNxHuwdZnyozEh74h8eY85GGv0 + z293tlZnw
9
vvNLvXf4KTGDF0UatnE1HA / Vti + f3xcC14bGr83yErpHJ70yIj + XQv2 / Gf /
yfsWwlPeTjxg + TpT61r3nmn3EivhasiWwedf3tQio8eP7D1cvt7hbZdh33S7
r9WLyjn2PNFGuOesrYPOXc / XYq8vMzpWIN8 / btnWYY4N3FW9eOv3vyfJ1 + tq
tOwQ8VOmljq5UbeI + nbCNxVvGHLHyjBPH3MKLOphLjwyas2jkokJWpF1F23s
h2rCS / 7
oMD4iNFtTTX9pNMXZTHW1juu9 + ZKbKll1qIHV9b + 1
SZGlQ5cowzzv
H5b / dONtjX4p4pvl39wzxDmOnzXbjteFH / 6
r7ZrQTa6qZJN3tyYvs4R / 2l
Lx
z / Iwg + / 6L
eTl4YfCpx70sFic4apUnEWAU7NzwguDftLP + OSivJMyxpV5 / iWc
8
Qn95MPDde + tNMyjy2Ift4 + 4
pm39supweaKT0h2emP799BzttmPTiMMfnFTJ
5
ZYBJ0tzhC / +zut + h2OGeTe66tCYG3eFd06rulLdy1GVPAmN6tRe + sL0vQ2v
N3IxxOkN4hLLM4T / 1 + eLvLHmUqsuhjgja1fetOtLhPP7ofP7p / P3S + 5
WFP6p
zEzlRBsl1VnppLzzesYtGV9NtRqY1uen3U6KHpw / 4
mzpZgtlscwmqqqjdO + i
kDGRey2UWVit6KpA6Ut9Yw / WemsYJ / Ifrf3JzUV41kfdwz + 8
zFVIWdDiRRHS
Q3x00zuOMVcHd05P77RFLzw8vmbrG4mWqjLUJGeKq6Pw05 + S5l2aYmYY / zM9
bcPk61N3btef9bBQnfeGLH6 + Vf772U + Nk8J2mqgdz9 / dquXhqF5Vb9W01x1T
tXRm / +zJ + S7i76Mz / qHz76czvqIzfqMzP6EPPbGzm5 + RsQrs + r2jlyad34 / 4
9
xFf0ita3FvW0dFIvZrcb8t8nYvIR5nf0sdkfN9k2mh75bq6lWe8chXO / Joe
Y5L8oflfdiow + OTsAk3 + +8
x / 6
cxv6awP0J3rzTvSK9FBea93Prpsqfz3J3Vr
1
Xp / jJ3y / zGnSY0JzuJ6rrRb2HbNciv16sPYV4 + bOArn / UHn / Uvn / Uvn / UMP
8
Fk23NbXQg3 / WbP7NMRBeKRPdMz40TZq6OcJy + afl87xh27hrk8ZM9ZejZq4
fO + 6
Px3V3QVbzHbecFY / NH9mVjPAQe1zqaj20t9ZpVqfuv / XLXvh4TUyu9u +
cFbHLd8any5zEN7rktVfrpddVHhWZc8 + BfL13jNbbuo9zlnN3d9h + +MZeuHn
u / hu / vZbV5X0 + XTQsFPy / SOmRvZ3NDXkCQcjpg5ZK18 / aXa3hQVRzsrb5Ldp
tpa2wid / fcar5RdHpRtSf8zpm / LzpXWLy / F766IuZZjMOXdXvn + fwEF9XqUZ
8
gN9gySbgQ5ivOL4Q + fvQ + f4Qef4Q + f4SOf4Qz96yabt + AVGakfvDXXrz3MW
zvFnaWKr8e / aOaryo00X2B83XF8N3E4F5epVYmYrVdvYUfhgx0UJF / P0ytQ +
8
VbpK718vbZpybg1TmpH / VrzddWchK94eHfVk3zD + LH94LYa2fL1vD7ozM / o
UWZv8id10av7Bzp4tJvvIJzXr / j8uL / okw9eavCtpV6tf1NcOMhwPXE + XBF /
vnbNqSYqc6 / luJeeejlfNhq6uWEjUxVTfmTj2Kvy9Rxf6EXDqr / KX2mkRn00
7
p33o5yPI + vra7t3MFL1D2a01rpI5 / VLN82MvzSqrk4d / 1
Kywu57 + e9zfBWf
b0z7cd1cTQ3zx4iRm60dRL2O9Tk641s643c660t0xvf0sMCp3XdMcVMX / 7
y6
ZcYL + flYP6SzPicc9TeLUafLG2 / 6
rDnbPGo4L9NWpfi8ft3hZJWWsG7w9cyx
tsJvDCp9GdFXp4au3dtg0js74RaTXvUwffleM538MFWfK18 / tLf160VVOhVz
u / Zv9 + zshacW99ozalq5FvMg8 + DT51bCEy7cKL830Uh5 / Hpm0uU6NsIj / Z6O
Cgr8pN3w99j5zVpL4YlnnsRWXCvTSlr8nvZus3x / j / sn49SZMk0dqH + zdIZ0
i6VZ11ONyrXAGtNntnvvoHKOftxlqrkpi2aDE984lWkOLRudPGRtuE7Kh69e
srZco / efGuyb09Fd5X / 1
rKvP8jfC86 + dM3o4y02dzlo + yG7sJ + E / HJ03aP1Y
d9VnydFmTbZUCM96 / LXZncNuKvHIdDPrDp + Fz3w84GNFnpsKLp5hV / SX9E / 7
for2OuWuUn81G9E945Xwxp / GV31xq64KrVv0f9e + RPjdju1avKxZXbXolLOs
eu4H4Spp5axb209ocbM3h9z4tVzrfnFw9Q6Rhvu66aGWBRvKtMw9s3wc7uiV
9 / Q646 / ueyt8Vbc + oSHVDOPI6VUpHWpKL7JROz089GqFX8 + mv1qUCc8KuZXx
KUqvPAOvxQ3KqxDu3 / Pq / IALehV2 + UbD2csqhZfX676 + 01
hH5TD6jpP1yirh
bc5Hjhlfaq9Svn682KKz / HzOfpsnePRwUO66OrPa534W / nSy87YW3g6qa85l
055
b5PuPHd1k + gxXvSppe6lHt + 46
Ea8W5m4qjX5qq9pYXoxp5ussPOBns99r
j7JTjSP92kebSmd8Tuf8RG9Tv7jN + BMO6qLKf + Y9Qb6e8Ted + QWd8Ted8zvj
IcYfdMZHdMY3dM6PdM6PdMZfdOaXwpH / hYWHPPnxzj0t6tekwIDsaqI + RY98
+ jnhu / PnNM + r9pYLNpkKd7DWVnsn5msrWjtG / GSYd + kVMxaezVtcqKVH2xem
+ ZsLT3ib0LbYu0CLNJlsMzVHvp71QfH5UH + j6xb + 8 / ml12btotXA2Q2uyc / P
+ iU9XPfyxIudLzSHsWOWzHhoqsIPBThZfDRROVbdT / fz1Kmlc6ZPXuBtbLi /
y + fd9avU6FF1f / ilzhETFd7v + pLjgSbi9cFZtba2bmP4 / 28
prOWzXLpp78zM
3
WcNn8N45 / 32
m6XrhszwbVLTTHlMHVB75mj5 + cISl5S / 6
vmPVjTT4aDHYGPh
ZStO + i03XP9 + dYoe5XSSr5 + bY9Uh / E8LFRfwYFWHC / L10w99c6DPczPVeMOR
czO / NhNe8iKvsPi + kQoe33hon3gzNWnmE2ubR6VadsPo69ZTrMT8Suf8TGd8
QO / Tq53vQuP3WpDv / YvLYyyEN / 7
zcqN9bm + 1 / lYjD / gNtREe9MP22NJqb7Qr
hcl / PE2yFs74gt4193iiuXWxllLzUe7IJ + bCGR / R444sDt / R9ZUWVtStZmod
C5XfQLe0pb2pqixOm17qba66NjM9tPWnasrCZ0tDXYWZcK95 / g / ml5iogF1J
tj5 / yNdPin1jem + c4T780P9BsKX02DWbu / w82kS53 / 6
yfH2u9HpTpvaLzDdV
3
rObb19bz1I4f396vNe7hDsHTFW2yehHJbPl63l90WPct3d2OKhTWV9n3lzs
ai6c9wfzReaXdM4fdOZ3dOZn9H0X69f1H6lXDu0yN1dV2MvPh / yVzvyUnmx7
39
f8GwfVM2JQ2IgN // L5UL9gvML4ic74jM74jM74i874i / Mh6690zo / CMT / S
WX + hMz6gc32ezv4AOusrXC / g + gKd6xN0rv / QuT5CZ / 5
K5 / oLnfkznesvdObH
nK9Dnraw + LDrpbaieeu0Og9NhDP + oDO + oTO + Ea8 / WVDN / odCzcHy15hJQ42F
c36gc / ynM36jW0z73vKbLc + 0 / iuizupHWirmY7qSW8W76u3SwvY7xf / j81Hk
a8zP6Mw / 6
cx / 6
Qn3YtSwJZnapF0PfA6v / yRfv73V3Q8bMrXIJsNLYy9 + Fl5 +
/ 6 + FD9 + 4
qySTQUsXX6sSzvyWzvyYzvyb4wXvXzrHHzrHLzrHFzr799jvJPqr
4
F43g9Ne136h5X97fr65h7NwXdiEm9 / FFWm6uAMVo3o7CRf9XXDW1 + iivwvO
/ iq66E / j50d / GOcbzi90zn905u901gfozO / pnF / pzP / pnH9P1v3SLHedXpV5
vwlYttRMlbfY8mhhmqPKHpbW6t5AM0UPGn / HJPWIo8pZpeVVRlYTHnzzS + r8
VMN / j8r9rcd7E + Hhx0YVhyxxULpTgce / d7IU7jlzrNXA / zmqxmmWlm6N5etj
N45zGPeVk4q55T + yx68Wwl0vr / q71TYHld39baHuuHz // jX6Jna8bq / U7qsb
DjWWr / fyWF7rTC97NcbkcPz4BfLv1yVb7zbd66RCoi2XT5hTTfy36I + Bs / +H
zu + Xzt + Hzv4jOvuX6Oz3ofP7p7N / is7 + I86HnH / pnH / pnN / pol4B5 / xJZ / 2
D
zvmfzvoDr0feH3Ren3Re // SwZnccTa3tlHpUlVGtt / z3B5sHHSqq0quhA7qn
PRpvLTy9f + 9
eI89ZqbLC1boj9lbC3TcuMy98a63Sq04PfThAvv / R8O2Xmu + y
UkmnH3aY + FF + Po4fXE / g + gCd6xN0rg / Qub5ET6qaVGOesSHOm3Z2g2UrO + HB
Ba + 3
RxUarvtmexas + EX + +1
x / oleYP3 / 3
SKvSdjSLqG4ULf99rt / 1
Se7glzfR
SV2xjdxzo62tSh7i4vr8upNaceFPi / i51sK5fk1n / kfn + j2d1w9drHfDY1Ys
mZwS66ICfjrcOy7NRjjHH / H5kD / T2T / gsLn9uPPZdsr70euno4Y4qBUvipMy
8u
1U
fq3ONj // Lp35M539E / SQoWNigjbYqfAyo5IzB2yFsz5Av5L6fEtzw / sX
nu177 / Ir + XrWH + j8fsTfj / oGnfV9vh8 / P52fj87vV7w / rk86P79w / L501n9E
PQbXN39Pvj + dvx + dfz + d1xed3z + dfw + d8wedvx + d8xfrgazv0VmfpLM + SWd9
ks76KD2pwaDS3l / MVQvfxKLOVfL1rD / SWd + kh6ddWrP5RTXVeF6rEzvm26p8
a + tmybYPtcLIU9d7KZn / 0l
VUeK9vk + 5
pwXecP7RMfyec + bF4PfJ3OvN / usiH
+ Xr / aZOcbhZqfYpXL6w28JVwrg / TWT + gM7 / neiDXJ + lcX6Szv5HO9Us6 + w / p
7
H + ks7 + RzvVb0zazJpr3f6cFuO7x + 9
TCMC5uGmHmM / yNtq / gYtvnZo7Ckwpv
55l
r77UVe7WTV0bohfef + b / Poc8Mv1OtZ9UrTsrX6 / Z2eXzVr1i7OLP / 3
y7F
DsLZ / 0
BPaZqb3WTGR833TlXJjBH / 8
v6oL9BZn6AzfqKzfsDPw7 + fzven8 / ul
8 / sR3wfiTzrXh + n8 / elcfxavx + / L / Sjcf0Ln / hM6808695 / Qmd / SmX / SmX / T
ma / Smb8yX2T + R2f + SOf6tshHkf + K98f6N535NZ35qXCsj / P74PdPZ32Ezt + H
zt + fzuuLzvoSnfUX1lO5v4zO / dF07m + mc3 + ecNSX6dzfS + f + Zjrry9xPyf2T
dO7PpHN / JZ37H8V + TuyfpHN / Jp3918JRP6azv5fxLuNnOus3dOYXdOa / dNYH
6
by + 6
awPiXo79j / TWb + nc34Xjvo8nesLdMYH4v0xP9Lnbg8JSBjsrnwD6n3f
IE8vnOsnzCeYn9CZP9CZ / 9
CZP9HZ30Dv6bn8k2m + ufKO6mS + 8
Vw14cyf6MyP
Gl9p9ajysq3yXjblVadaXzRdL + 3l
qVm2am4XO332fCPhXN + gew4M + tBgkY2y
8
Zvdr / FQ + Xqur9A9PscOc35pr1TzpyPWjZOv9 / Qd / vZOibXqGe / m / DLTWDjX
T + iRK / uNyhhgyL9fbDh12DD / 0
v2 + tCko9LRRk3a23lYnVnqTb8fP2f + 1
Xp3 +
rih98igjxfVsrq / TuX5O5 / o + nev7dO6 / pLO / gM71f / ZTsj + SzvmHzviVzviY
zvmPzvmbzv0J7Mfh / EDn / ERn / w6d + 0
PorF / Rub + KzvmZzvmX4wXHLzrHLzrH
TzrrK3T2f9FZ / 6
dzfGY9g / UXOusbdPbPi / dHfYbO / R101o / YD839hXTuL6Rz
fw2d9Uk69x / Sub + Izv2 + dNan6ayfMF5lfEvn / UHn / S3OK8H9Q2f8S + f4Qmf8
yn5i9h / T2f9LZ / 8
xnfEHnfcvnf2adPYv0xmv0Dk + cL7k / Evn / Evn / Ejn / Evn
/ Enn / Exn / xzHA9aH6az / 0j
k + 0
VmfpbO + K94f4yud / Vvi70N / GfMl5kd05kd0
rq / Smb / RWd + gsz5CZ / 2
D3wf71 + jsX6Pz96GfX3R63kYLN5UZtn / VkU9fhPP3
p / P3ocdWmqz7pdRNJUQPv73yrE78fSlVfj5vprmq1LWbOjVvK9 + f1y / PM + L5
SHSef0ZnfYbO + ZnO84foPL + NzvoOnfUpOs9n4nlePN + QzvOb6Dzfi87zD + ns
j + b3zb + Pzt + Xzu + Pzvocnb8PnfkD6z2sr9BZP6Kzv4bO / JTO / JTO / hs682fm
U / z76fx + 6
fx96dzPRmd + SefvT2f + yXqXOF8QLvpX4aI / Fs76E130t8IZP4rP
z / 5
dOOtn / L15 / dB5 / dF5 / dJZ / 6
GzviSuR9xfdO5fo7N + xPmY8zed8QOd6yN0
xid0zv90rm / QuT7C9XLmR3TuD6ZzfZ3O9XM619 / pzO / oXH9nvZbXN533J533
D5397XSOD3Te33Se38B + R / ZH0ln / EOc5YP8hnfsb6dx / SWd / JJ39lXTu / 2
Q8
xfiNzviMzviBzviJzviALs4nxnjB + 5 / O + ZnO + 5 / O8YvO8YXr / Vzfp3N8oXN9
n / 5
f / z7HTzr / PjrPb6RzPZj9GuzvoLN / gs7 + Ejr7S8T7Y / 2
KLs5XgYdYjXxV
NL9Yc3caPiTQy05xPwv3l9C5f4TO9Rk699fQuT5E5 / 4
ZOtdv2C8h9hfAxf4B
uOj / h4v + fzj7K8T7o3 + D + Tzzdzrzdzrzdzrzczrzbzrzfzrzezrzd563xPoW
nfUzOveH0jl / 01
m / o / N8Jzr3q7Jfl / 21
dPYH09n / LBz9yXSuH9HZf814ifEN
nfkTnfGPiMcQ / 9
CZP7GewPoEnfsv6dy / SWf9RNQz0L8j3h / 7
Oenc / y3iRXw /
dH7 / dP5 + Yj0B1zfzQeZ / dOZ / dOZvIt9Efkhnfkhn / kdn / kdn / wTrFaxv0Fl /
oLN + Qmd8mb9pxeoz9Qxx3sE1gycmPhPno9N5vjqd57vTj448tC91gpEquTKi
b5pDiXDWB + mMn + mMv + k8z50unreA + ZrzL53zL53xA539m3TGn + Lzob + S873o
j4dz / qZz / qdzfqdzfqdzfud6ONe / 6
Tz / js71J + FYP6Lz + 6
FzfwOd379Y70f8
wv8W6 / twvj + d63d0 / j7i9fj7eZ4Ez5 + g8 / wIep9pMydMs3yqpXy7e1vXOdIZ
H4vX43wmOs9fovP8fzrPl2I9hPUJOusrdNYv6OyPobM / hs79RNxPy / 259
NhG
LW + 7
OVup + K / bvz01Qr6e / X30NotcNqYPs1ABO75q8INhXqRzfxud8yed / Td0
7j
ejs3 + I / SrsL6GzP4XO / hk6z8 + ls7 + Gzv297Kdg / wVd9C / B + f3T2R9CZ / xE
5 / fPfjz279G5fkPn / hg6 + / NEPyDqK3R + / 7
zeuX + PzvuPzvuLzvuTzvuLzvGD
zvGDzuufzvFRPO + E8RVcxD98PeIfuoiv4IzP2M / D / h0683s6 + 3
vo7M + hsz7B
+ YC / H533F539VXT2P9E5ftB5 / Yrn8eD5OXTOz3Q + H4jO + ILO + ITO60d8flx /
dMYfdNZXOZ5wfqDzfAg65y86x0c64xc64xc673 / W + 1
m / p7P + T2f9ns71BzrX
B1jvY / 2
CzvufzvuXzvoLnfVLOscLOvv9uJ7K9Vc612 / pXP + lc32VzvVbOp + n
Quf6LvMV5kd05ld05pdRPYoW9gj9oEWWxH / dekc1FbR5QsN87YPmPHzn5YIN
hngIzvyEzvVROvMrOvMTOs / zo3P9gs7 + WTrPm6Vz / VXst8b4Q + f6F53ra3SO
X3SxPwTO8YzPA + L + fDr359PZ30Zn / ZnO + 0e8
f6dxFgfnOihdwlf9ys + li / dn
/ ZnO + zd2W + 7
INT + 5
qqInJy7Xb2sjzt + h8 / l5dJ6vQ + f5Q3Q + / 4
b + 7
vox / due
7
sor72 / LI7l2wvl8H7ro34XzfCI65y9e77w + 6
Zz / 6
bx + hSM + YLzB86vpjF / o
XD + mc32bzvGDzvGDzvGPzviRzv4T9sNxfUg8bxX7M + jc / 0
Hn / hE69x / Tef3S
eX + I / SJY3 + H3ye + fzu + PzvmPzuuPzuuPzvlTPG8F1yed8yvXG7i + Qef6A53r
H3Suv9C5 / kLn + gn7edj / Q + f + Ujr7i + jsn6DzfAzx / ujPYL / Hfzn / fTr7S + js
H6Hz + 6
Fz / Y / Ov5fPG + XzSenhneqdsDSM + +lj / KeMtb4hnPUDOud / OusbdMYv
dO7n5XjE8YfO + Z / O8Y / O / al0js907o + lc / ym83xDrlcxf6Az36BzfUo48hc6
16
fozC / pzJ + 434
D7l + jcj0Tn + EJnvyGd4xvzFe5PFPkM6td05nd01s / orJ / R
WZ / n9c7rl87rk877g87rn874hM77m877e3fas9 / yjhjy9g5DJxf0qRLrx3Su
P9O5nkxnvxid + 8
HorA / RuX5N5 / PK6Dw / mfEM4ys64ys64zc6r0 / xvDvET7yf
eP3TeX / R + e / Tub + XzvuHzvUmOvf / Mt9j / knn + Ednfkzn / EFn / xyd + Sed4yvj
IcY / dMZXdMY / dMZPdMZ3dPZnsd + Y / cV0xmN0 / nt0fj7m48yv6ay / 01
k / p7M +
QGd9nc71OZ63wP5OOtcP6ewvpf / Xv8 / 6
rTiv9j / W07k + Lhzru3T + PnQ + v4fO
/ ko6n1fM9SKuL9G5vkXn + iid9Q + 66
C9HvxD7g + iifg4X9Xe42O / N90f8Sxf9
4
FhPFN8fnPVBuvj + 4
Kxv0sX3DRf1Mri4PuBc3xTnXWN + oYv + cTjPF6JzfqQz
vqSL / A3xHuNDOuMvOq9fOq9POvMzOvvlWC9kfY3O + JnO / mo68wM643E6r386
81068
w / Gq4w / 6
YxfxfOaEX / SWT + ks34onreE / nw6 + / vp3P9Nf1W9VdNed0zV
0
pn9syfnuyiu93D9hc71HzrrO3SuT9FZX6KL / RBYb + P6HJ37z4RjfUDsl8Pv
T + f4Kc6rxnoIn7fK / ITO84DozCfozE + YT / P + ofP + pvP8KDrPf6LzfuZ6Evvr
6
Iyv6Ix / 6
FxfZb2A4yOd8wed8x + d + Rmd8xud8xv / PX4 + Ot + f / l / vz / mZzr + P
+ RrzMzrzLzrzQzrzSzr359C5v4fO / UP8b + 4
fovP9xXkU + Hx0fj909r9yPOf4
T + f8Q + f4Tmf / DOs1rL / QWR + hc / wUz2tG / yHzBcZfdMb / dMZ3 / L35 + 4
rzRPD7
0
vn70vn70tk / Tef1zPGO8Rmd4wud8wfzCeZHdO6 / oDM / ojM / 4
XkK3J9G5 / kM
dO6Po / P8BDr339G5n47O9V / 2e7
M + Q2f9h876Ep31FTr7g + msF9G5n0R8fvT3
sp + T / Zl09sfQWX + ns7 + T3wfrO3R + v3T + PpyPOf / SeX / SeX / SGR / yfuX9R + f9
R2f / M531DTrHB / YjsH + Bzv4HOvsv6Lz / 6
Oy / EM / LRf5HZ / 2
PzvyPzviX6 + ns
r6Nzfqez / 4 / O / JDO / I / O / mDme8zvxPOAkH / RuZ9GvD / yQzrzCc4nnB / oHP / p
3
F9N5 / Mw6Jy / 2
G / L / Sd03l909i / RuZ + Rzueb0vk8F64ncf2dzvGfzvGczn59
3
q / i + dZw3n903t88z4LnY9BZP6WL89nhXD8R57FjfYTrHcy / 6
Zz / 6
Pz76Vzf
oPP7ZTwszj + Asz5C5 / 4
icR4f4nex3xDxO89j4 / ludI5vdNZnxesxftF5Hgnv
F8Y / dMZPzCd5voHo98Z8Sed8xvVQ5v901hforA / Qeb4WneMP70feX3Te38Kx
Psp6GutvdMZvdI4PdMaHdMaL3E / E / Ut0rk / QeX1zPGH8zHiP8R2d8R2d8Rud
8
R + d + R / nY76ezvND6OzHpf / XecKMP + iMP7gexvUvOusrdK5v0dm / RGf9hfvF
uD + MzvmNzviTzudd0sXzJOC8 / +msn3G + 5
Pwo5lPMz2K9BfE5nf3BdOYPdO7n
oTO / oDO / oG / 9
supweaJhnjs8Mf376XI9yavr / Zcbdlmr20ljNoQ + dhf5Oucv
Ouc7OudHOvsj6OxPZ77O8ZnO8ZnO8Z / 7
Qdl / S + f + Ujr3l9PZ383rTezvgov1
QzivTzqvHzqvD643Mb6n8 / 6
ic / 2
Vnv3UOClsp4na8fzdrVoe8jxrxn90zo90
xnf0 / DeXCn1upmu + PcN3Lu3kIvI91m / orN / QmR / SmX / SWV9ivM76P53xO535
AZ3rD3T2h9K5 / sDxnvGhyPcwP9EZH4r3g7Nfgf0JdPZP0Lk + LhzXB53Xl3D0
ZzCeEM9vwfXE / jI66xMiX2L + xfNy8ffTxfMc4fx7GY + J5zPA + bwMkQ8ivmY9
ntcnnfV1Ou8vOtfj6Fyf4N / L8ZfjAa8fOq8 / Oq9 / 5
vPi / H64OL8fzvyS8T7z
DzrzF + 634
vxH5 / xL5 / xN5 / mvdMYHjDcYn9CZv4p + Uty / dK730fk8bDrjP + YL
HH / pzA / ojN / pon8Y9wPXf + jMf + ns36bzfCU6nzfIeFQ8nxjO35 / xHOMzOuND
9
oNzfqPzfCs619voPN + KzvmWv5eoT8D5 + 9
DFeAzneVfsp + Dr6fz96Yx / 2
A / A
9
Tk6 + zdFv / OPFbbvHx / XgteGxu8NshLOfic6zzOii / 4
C9HNwf6J4XibPw4Rz
fyX7ndhfRef + GTr7Kej8fun8fXg / 8
Pqmc / 6
nM36m8 / xDOuMHOuMTzsecf + mc
f1mP5PxFZz7LeI / xMZ3xBedzzv901h / prO9xvOT4Suf8xXia9T3Ox2J / AJyv
53
n1zD / p7Hehc71TPM8G9WQ6652MB1ifobP + Q + fzjBhv8fqjM36js34jrjdc
n3TGx3TG14zXxPOV4YwP6IwXOF6yniXO48H + btZDuX5E53qsWG9EfYf5IPu /
xX4c7L + hc3ync36jM57l / cZ8WdzPPP8Z + WJE3EnjZxdc1dYVNS + XZjqJ64HX
D531H45HHH / 4
fnw9neMPnef7cDzl + EtnPkbn + gzjAfaL0hl / 0
Pn70fn78fti
/ YTO + 53
O8YPv91 / O8wuEczxCviX6E + CDHRclXMzTK1P7xFulr / Sin5zrw3Su
39
IZP9AZb9CzQm5lfIrSK8 / Aa3GD8io0xkuMf + iMv + iMj + isT9IZ / 3E+4
vxC
5 / zE75vfH53fP + sZfH86z5 + k83wY5mMi / 8L
3
ze + Hzu + fzt + Xfy / jAzrjDzr7
t / nv8fPxfuR5C3QxXsC5 / 4j
OfJLO + ivnW66f8LwD7uekn6z7pVnuOsP35f0m
YNlSM + Hs92I + wfuZ9wOvP14v / D3o / H3ozM / pzM95HgHPH6Czn4XzIfMLjvf8
/ ViP4XjN9RqOT3T + fXR + vyctO51 / mK5X0z / cchgTJc / HqHQKOPR3OxfV / UBg
6
oj9enVyYHPvz6tc1JeZ / 6u
Y20evIo9u9Upec0zznl3L5UGc3A8f0mHpRps2
rirm7LOFG88 / EPG4g1eff5Y3e6hdNPV / XLd6qawnDPhu8ro5Tsp / 1
taTRr + 5
q7A1F + q12uykks4 / 2l
ta5K7eNfVtPSjMRYWMnLwjvpc837Iie5Huq1IjNXd5
81
mD + luokuZrNwZ1NFanu47 / Lu1nw3x9McfqUuRHrfHddg31Pm5ivYD / e9bn
Vc / IkvX79MoxObfJYp2rcrUpqL65lV49 / Bh2NuCyi1K13PPL + +VpDz0bDalR
Q + ZbuiWJ5yJmGq6348k / mR + sFNcf3S + sidebJL2q2DwxasvuKm2qe + mQr1IN
84
VP7U9jo + T5wHSex0vn50 + wnmtlGfmnluK3 + k5BnWItLOds84 + OdzXP4LKs
NxOKxefh5 + 9
zPXRHzscyrex45fjNLeT5N9lXzJ9uf / xZCxn / +53
pzx6J + DHs
WtbLwUGuKvLh7n03118S82lq0Kz + 75
dXUyXfPavpfUHu11BGXb8xqTBSXfvX
TQhs5yzWkzfdqlHc56qjUg1SvukYliXmQ13YNUujSzFavf4bfr4 + 8
b2IT70e
R2yft + qD1ub3Qwu2WsrzNScl / bn + B087lew88V6qXsY / MbqaE6122ivj34e1
Dvko + 98
avzrxpVuDt1ryqIS83JNyf27sL / 1
q3 + jqpvymHNrYL12eV2m63zd7
uq + NOhoQsvf4cbnfjs7nYdG5H4rO5y3n + I9uFv234T7Z3jC + S4dc8Tx4NWKY
i + vGTO1Gj / cOWyvk + Rr5k41iXh60Vm0ed3OuG2Ar6snuAW0dtpV / 0
RKubsjK
6
v0vz5 / aMs + 8
zRRDHPFrnHGPr + Tz4IJfj3kwcbqJyilfldfYWtaTE3yvL5k0
+ obmUJQeWKefu1LrXfxt79zRKl9HThw6311dfFCe / zTVSnn / fCuqce4dsR + b
XtLzVmylkbUqmV01LLlZruY3zz90fRdXlfHTlG6PvnZWuh / 9
xpQscVXNsrvc
OhDhrAKn + lqNfmcYh961SfrtT5nPVhwbYJ81w01lvXke81fUJ3G + Fj2m / etO
Dba6qfQGpXnbvkjn + Rx0nv / RXjnNvdPPVaVciPc3b5Mnxnc654PdfYMb9urs
qLoOKZpX7TfZT2oxKmpLdJC7Ksnc3vzTMCORr7ubL1gzO9vwfZwojRvboUzz
dd + 1
feZNd3XlgksDy7mlGp33s43rnkXthzmqmVHXB4T + 4
qx + rhdSe3qmIb7Z
tvnb2 + OdVcIPGX9aBl3VQr5d + ePVf3keWLBXTGDIwWoq5tSXZysmyvo / nfHL
w2 + eRo8bqFcJpqk + 93
d / EeMpnfMBnfnC6YFhG41Pu6mDa / N7zN0vxws6x4 / T
c / 1
aXLr6f33ZMw786lso6ql09nPS + Ty32Iijs99dMdz3KQG6PVEyX + D1yuuT
zuufzus3eVntDu9Hl2l9Vhz88mKkfD6VcMxnKfbP / R3iHFTUpNU1rs20FOcd
0
sOPjSoOWeKgdKcCj3 / vZKkK / 4
xN2GyIr3Q9jvW9 + XqPyL84XnB8mX44MPfc
OivVPjv0 / XzDdRBzLrLH782s1Yo2iTuDnzsougp52CH8tZVKXec9Puv2 / 50 /
1
mLcGG8T9SnPa34vCxeV / Out5iXXTFTi2KaZJU + cVcnY1 / 0
CkyxU3IBMdfaj
XoXH12x9I9FSVYaa5ExxdVSjSq3f + 7
xzVklTjyTYhziI9Rk665NB6x137EzQ
qfbjLg5s98xZVbS4t6yjIT96Nbnflvk6F + U99FbZPO + PWvyWp1naIHkeXosF
J6MLfnFT2etSTN / Nkr8 / neMZndcLndcfndeXv493jRvznVSMV593K1ZbifPe
osK8lgzKNFKNXxZn9WppLfZvep4 + te / vLpVaeugvw9xbnxD5RdKhj2ct9 + tU
// SuJrcb69XRmQdch7sYqaG340Nd / fWKLp6vlKA17jHkglaclrPZzEX2v / H9
+ HqvMemh6 + q4Kl3tBbun / W4qnrdNZ38Bnf2erbL1 + Tsi3FWcv8ecY03l8055
vfP6Htr + zCaf3a6qKDt2UmJ1E2WXmn / 0
aXtDPOkZcbrtHENedLNugZeHrfL4
dmV0yT0Zn9FFP0vygW31RuZp + U9mXTpZ8C / 15 / qTa + 90
rtRCNjh5TFwrn3eQ
/ G7mBYdOzqrN3fuqcz9bUa / XxSwaPnhwsBbT9HG3tLqVon8reO2n7MEr7FWf
uuNc2jXQi3iyTcl3 + wvH2qjsvZPShtVyE / 0
VUWmRpUfHftaSkuJtTU8Z8vku
adPqzKvUcszcwxqPN1P / DwJR1mM =

"], $CellContext`edgesNNadj$$ = {{122, 163, 228, 188, 256, 154,
14, 177, 95, 240, 200, 204}, {56, 218, 98, 36, 215, 153, 76, 257,
                              78, 196, 5}, {20, 243, 169, 92, 179, 196, 195}, {96, 192, 94,
                                                                               83, 216, 254, 37, 237, 79, 59, 206,
                                                                               243}, {153, 36, 182, 95, 176,
                                                                                      32, 75, 175, 163, 2, 99, 188}, {
    68, 57, 157, 223, 247, 96, 251,
    126, 191}, {221, 76, 74, 284, 128, 175, 194, 239, 98, 85, 99,
                195, 259}, {278, 116, 171, 187, 53, 87, 201, 55, 244, 81, 40,
                            137}, {146, 174, 168, 114, 219, 252, 148, 224, 111, 54, 232}, {
    280, 203, 33, 245, 266, 70, 92, 112}, {222, 268, 131, 282, 112,
                                           62, 70, 245, 33, 200}, {276, 145, 184, 17, 199, 107, 15, 193,
                                                                   249, 19, 67}, {17, 32, 199, 176, 182, 257, 25, 249,
                                                                                  36, 63, 153,
                                                                                  205, 276}, {1, 256, 50, 228, 82, 177,
                                                                                              240, 122, 274, 24, 118,
                                                                                              163, 198, 225, 439}, {12,
                                                                                                                    67,
                                                                                                                    107,
                                                                                                                    145,
                                                                                                                    184,
                                                                                                                    193,
                                                                                                                    172,
                                                                                                                    144,
                                                                                                                    276,
                                                                                                                    263,
                                                                                                                    405}, {
    160, 202, 159, 173, 132, 227, 248, 149, 136, 167, 44,
    123, 140, 234, 407}, {12, 13, 199, 276, 25, 257, 32, 249, 205,
                          63, 145, 158, 176, 182, 184}, {183, 30, 64, 209, 227, 191, 190,
                                                         173, 263, 93}, {12, 115, 143, 193, 158, 109, 276, 124, 107,
                                                                         269,
                                                                         205}, {3, 243, 92, 280, 237, 203, 117, 169,
                                                                                192, 83, 365}, {84,
                                                                                                43, 238, 270, 152, 105,
                                                                                                138, 285, 127, 88}, {
    119, 260, 101, 212,
    91, 73, 133, 102, 35, 165, 137, 197}, {142, 283, 89, 38, 130,
                                           189, 31, 141, 289, 267}, {14, 225, 198, 82, 263, 118, 274, 50,
                                                                     67, 209}, {13, 17, 63, 257, 205, 158, 109, 32, 182,
                                                                                36, 78}, {54,
                                                                                          100, 90, 207, 213, 168, 111,
                                                                                          242, 146, 34, 41, 180}, {156,
                                                                                                                   288,
                                                                                                                   69,
                                                                                                                   208,
                                                                                                                   108,
                                                                                                                   135,
                                                                                                                   139,
                                                                                                                   185,
                                                                                                                   273,
                                                                                                                   164}, {
    127, 285, 152, 262, 211,
    246, 138, 261, 238, 104, 120, 125, 258}, {60, 113, 287, 65, 48,
                                              164, 217, 273, 231, 108, 69, 139, 208, 265, 288}, {18, 183, 209,
                                                                                                 190, 93, 46, 64, 227,
                                                                                                 210, 149, 263}, {23,
                                                                                                                  89,
                                                                                                                  142,
                                                                                                                  283,
                                                                                                                  38,
                                                                                                                  130}, {
    5, 13, 17, 25, 176, 182, 36, 199, 257, 95, 153, 249}, {10,
                                                           11, 245, 70, 266, 112, 203, 282, 280, 62, 117, 92, 222}, {26,
                                                                                                                     180,
                                                                                                                     213,
                                                                                                                     90,
                                                                                                                     207,
                                                                                                                     41,
                                                                                                                     261,
                                                                                                                     104,
                                                                                                                     54,
                                                                                                                     258,
                                                                                                                     120}, {
    22, 103, 165,
    212, 119, 71, 147, 241, 73, 91, 101, 49, 102, 133, 233, 260}, {2,
                                                                   5, 13, 25, 32, 153, 182, 176, 257, 56, 95}, {4, 83,
                                                                                                                206,
                                                                                                                186,
                                                                                                                94, 243,
                                                                                                                216, 59,
                                                                                                                96,
                                                                                                                254}, {
    23, 31, 130, 89, 141, 189, 289, 142,
    267, 283, 264}, {181, 86, 272, 58, 129, 72, 134, 42, 77, 40,
                     277}, {39, 81, 187, 86, 181, 171, 116, 8, 72, 278, 55, 53, 129,
                            201, 244, 272}, {34, 213, 90, 180, 26, 54, 100, 207, 242}, {39,
                                                                                        58, 77, 134, 279, 277, 235, 166,
                                                                                        106, 272}, {21, 270, 84, 105,
                                                                                                    124, 230, 226, 269,
                                                                                                    121, 115}, {140,
                                                                                                                248,
                                                                                                                149,
                                                                                                                160,
                                                                                                                277, 16,
                                                                                                                234,
                                                                                                                72, 46,
                                                                                                                159}, {
    286, 210, 144, 47, 93, 229, 190, 46, 209, 263}, {
    30, 44, 45, 93, 190, 210, 149, 209, 286, 183, 277, 47}, {45, 286,
                                                             229, 210, 144, 93, 46, 134, 190, 58, 106, 235}, {29, 217,
                                                                                                              113,
                                                                                                              287, 65,
                                                                                                              60, 271,
                                                                                                              273, 164,
                                                                                                              170, 105,
                                                                                                              110, 226,
                                                                                                              231,
                                                                                                              281}, {71,
                                                                                                                     233,
                                                                                                                     147,
                                                                                                                     165,
                                                                                                                     103,
                                                                                                                     35,
                                                                                                                     66,
                                                                                                                     102,
                                                                                                                     212,
                                                                                                                     241}, {
    14, 24, 82, 274,
    256, 118, 240, 228, 177, 225, 198}, {250, 155, 178, 214, 88, 52,
                                         186, 206, 121, 59}, {51, 178, 121, 155, 88, 124, 109, 250, 158,
                                                              214}, {8, 87, 201, 116, 244, 171, 278, 187, 40, 55, 224,
                                                                     419}, {
    9, 26, 34, 41, 207, 100, 168, 90, 111, 213, 242, 146, 180}, {8,
                                                                 40, 53, 278, 81, 187, 171, 116, 129, 86, 87, 189}, {2,
                                                                                                                     36,
                                                                                                                     98,
                                                                                                                     218,
                                                                                                                     215,
                                                                                                                     76,
                                                                                                                     153,
                                                                                                                     196,
                                                                                                                     78,
                                                                                                                     257,
                                                                                                                     179}, {
    6, 157, 68, 223, 126,
    251, 247, 136, 96, 191, 254}, {39, 42, 47, 134, 77, 277, 72, 181,
                                   86, 279, 399}, {4, 37, 51, 79, 216, 186, 254, 94, 206, 250, 151,
                                                   83, 214}, {29, 48, 287, 273, 113, 217, 108, 265, 65, 271, 69,
                                                              139, 164, 208, 231, 281, 288, 384}, {236, 289, 220, 141,
                                                                                                   161, 80,
                                                                                                   267, 162, 97, 264}, {
    11, 33, 112, 282, 70, 266, 222, 245, 203,
    131, 268, 400}, {13, 17, 25, 205, 257, 158, 109, 78, 218, 276,
                     408}, {18, 30, 191, 247, 227, 173, 183, 202, 223, 251}, {29, 48,
                                                                              60, 113, 217, 287, 164, 231, 105, 273,
                                                                              226}, {49, 233, 102, 133,
                                                                                     165, 169, 71}, {15, 24, 145, 184,
                                                                                                     107, 144, 172, 193,
                                                                                                     12, 263,
                                                                                                     225, 198}, {6, 57,
                                                                                                                 157,
                                                                                                                 223,
                                                                                                                 247,
                                                                                                                 251,
                                                                                                                 126,
                                                                                                                 191,
                                                                                                                 96,
                                                                                                                 368}, {
    27,
    288, 139, 208, 108, 164, 29, 135, 60, 231, 156}, {10, 11, 33, 62,
                                                      112, 282, 245, 266, 203, 222, 280, 117}, {35, 49, 66, 147, 103,
                                                                                                165, 241, 212, 233, 73,
                                                                                                119}, {39, 40, 44, 58,
                                                                                                       181, 86, 140,
                                                                                                       277,
                                                                                                       187, 81, 171,
                                                                                                       134, 248}, {22,
                                                                                                                   35,
                                                                                                                   71,
                                                                                                                   91,
                                                                                                                   101,
                                                                                                                   212,
                                                                                                                   150,
                                                                                                                   241,
                                                                                                                   119,
                                                                                                                   253,
                                                                                                                   197,
                                                                                                                   103,
                                                                                                                   137,
                                                                                                                   147,
                                                                                                                   372,
                                                                                                                   391,
                                                                                                                   410}, {
    7, 221, 195, 76,
    169, 85, 179, 196, 98, 128, 215}, {5, 188, 175, 163, 154, 95,
                                       350}, {2, 7, 56, 74, 98, 221, 196, 215, 179, 218, 85, 169, 194,
                                              195, 239, 284, 414}, {39, 42, 58, 279, 134, 166, 162, 97, 272,
                                                                    80}, {2, 56, 63, 218, 215, 98, 25, 205, 196, 257}, {
    4, 59, 254,
    216, 94, 151, 96, 126, 186, 206}, {61, 77, 97, 162, 166, 220,
                                       236, 279, 185, 161, 348}, {8, 40, 55, 72, 187, 86, 278, 181, 171,
                                                                  129, 116, 244, 272}, {14, 24, 50, 225, 198, 274, 118,
                                                                                        256, 263,
                                                                                        240}, {4, 20, 37, 59, 206, 94,
                                                                                               186, 243, 216, 96,
                                                                                               192}, {21, 43,
                                                                                                      270, 105, 238,
                                                                                                      138, 152, 226,
                                                                                                      230, 285}, {7, 74,
                                                                                                                  195,
                                                                                                                  169,
                                                                                                                  221,
                                                                                                                  128,
                                                                                                                  179,
                                                                                                                  76}, {
    39, 40, 55, 58, 72, 81, 181, 272, 129, 187, 171,
    134}, {8, 53, 201, 116, 244, 171, 278, 187, 224, 55, 419}, {21,
                                                                51, 52, 155, 214, 178, 121, 250, 238, 125}, {23, 31, 38,
                                                                                                             142,
                                                                                                             283, 141,
                                                                                                             130, 289,
                                                                                                             189,
                                                                                                             267}, {26,
                                                                                                                    34,
                                                                                                                    41,
                                                                                                                    54,
                                                                                                                    213,
                                                                                                                    180,
                                                                                                                    100,
                                                                                                                    207,
                                                                                                                    242,
                                                                                                                    111}, {
    22, 35, 73, 101, 212, 150, 119, 197, 241, 253,
    103, 137, 147, 372, 391, 410}, {3, 10, 20, 280, 203, 117, 243,
                                    266, 237, 33}, {18, 30, 45, 46, 47, 190, 210, 209, 286, 183,
                                                    149}, {4, 37, 59, 79, 83, 216, 254, 96, 192, 151, 186, 206,
                                                           416}, {1, 5, 32, 75, 163, 176, 182, 188, 153, 36, 249, 154,
                                                                  360}, {4, 6, 37, 57, 68, 79, 83, 94, 192, 254, 216,
                                                                         237, 420}, {
    61, 77, 80, 162, 166, 279, 220, 236, 185, 161, 265, 348}, {2, 7,
                                                               56, 74, 76, 78, 215, 196, 218, 179, 169}, {239, 194, 284,
                                                                                                          259,
                                                                                                          175, 128, 221,
                                                                                                          7, 5, 389}, {
    26, 41, 54, 90, 242, 111, 213, 168,
    224, 146, 380}, {22, 35, 73, 91, 212, 119, 150, 197, 241, 253,
                     137, 372, 391, 410}, {22, 49, 66, 133, 260, 165, 233, 119, 35,
                                           212, 103}, {35, 49, 71, 73, 91, 102, 165, 212, 147, 241, 119,
                                                       150, 233, 253, 260}, {28, 34, 261, 258, 255, 207, 262, 246, 219,
                                                                             127, 180, 213, 275, 285}, {21, 43, 65, 84,
                                                                                                        226, 270, 230,
                                                                                                        113,
                                                                                                        217, 48, 170,
                                                                                                        413}, {42, 235,
                                                                                                               281, 271,
                                                                                                               110, 229,
                                                                                                               265, 273,
                                                                                                               47,
                                                                                                               287}, {
    12, 15, 19, 67, 193, 172, 145, 143, 184, 115, 144}, {27,
                                                         29, 60, 69, 208, 273, 265, 288, 185, 287, 139}, {19, 25, 52,
                                                                                                          63,
                                                                                                          158, 205, 124,
                                                                                                          276, 121, 115,
                                                                                                          178}, {106,
                                                                                                                 170,
                                                                                                                 235,
                                                                                                                 271,
                                                                                                                 281,
                                                                                                                 229,
                                                                                                                 217,
                                                                                                                 48,
                                                                                                                 172,
                                                                                                                 226,
                                                                                                                 230}, {
    9, 26, 54, 90, 100, 242, 224, 146,
    168, 213}, {10, 11, 33, 62, 70, 282, 266, 245, 222, 203, 117,
                268, 280}, {29, 48, 60, 65, 105, 217, 287, 164, 231, 273, 271}, {
    9, 148, 219, 174, 255, 258, 168, 146, 246, 125, 232, 252, 427}, {
    19, 43, 107, 109, 143, 269, 193, 124, 270, 230, 226, 121, 158}, {
    8, 40, 53, 55, 81, 87, 171, 244, 187, 201, 278, 181}, {20, 33,
                                                           92, 237, 266, 203, 192, 280, 112, 70}, {24, 50, 82, 274, 198,
                                                                                                   225, 240, 256, 14,
                                                                                                   263, 311}, {22, 35,
                                                                                                               71, 73,
                                                                                                               91, 101,
                                                                                                               102, 103,
                                                                                                               212, 165,
                                                                                                               260, 133,
                                                                                                               150,
                                                                                                               197}, {
    275, 262, 138, 261, 127, 34,
    180, 135, 28, 285}, {43, 51, 52, 88, 109, 124, 178, 155, 270,
                         158, 115, 428}, {1, 14, 228, 177, 154, 163, 256, 204, 188, 240,
                                          200}, {234, 252, 159, 248, 167, 232, 132, 140, 16, 244}, {19, 43,
                                                                                                    52, 109, 115, 121,
                                                                                                    270, 143, 158, 269,
                                                                                                    155, 178, 415,
                                                                                                    418}, {88,
                                                                                                           114, 211,
                                                                                                           246, 238,
                                                                                                           214, 28, 285,
                                                                                                           127, 219,
                                                                                                           152, 148,
                                                                                                           155,
                                                                                                           250}, {6, 57,
                                                                                                                  68,
                                                                                                                  79,
                                                                                                                  151,
                                                                                                                  251,
                                                                                                                  223,
                                                                                                                  157,
                                                                                                                  136,
                                                                                                                  132,
                                                                                                                  167,
                                                                                                                  254,
                                                                                                                  346,
                                                                                                                  387}, {
    21, 28, 104, 120, 125, 285, 152, 262, 211, 246, 138,
    238, 261}, {7, 74, 85, 99, 284, 221, 259, 239, 194, 175, 195,
                359}, {39, 55, 81, 86, 272, 264, 181, 267, 40, 189, 130}, {23,
                                                                           31, 38, 89, 189, 267, 141, 289, 264, 161,
                                                                           129, 142, 283, 310,
                                                                           318}, {11, 268, 200, 222, 204, 282, 177,
                                                                                  62}, {16, 123, 126, 167,
                                                                                        159, 136, 202, 251, 173, 223,
                                                                                        160, 151, 232, 234}, {22, 66,
                                                                                                              102,
                                                                                                              260, 119,
                                                                                                              233, 165,
                                                                                                              35, 280,
                                                                                                              212}, {39,
                                                                                                                     42,
                                                                                                                     47,
                                                                                                                     58,
                                                                                                                     77,
                                                                                                                     277,
                                                                                                                     72,
                                                                                                                     181,
                                                                                                                     86,
                                                                                                                     272,
                                                                                                                     399}, {
    27, 69, 120, 139, 288, 275, 164, 231,
    208}, {16, 57, 126, 132, 251, 223, 202, 173, 157, 167, 159, 151,
           227, 247}, {197, 150, 101, 91, 73, 278, 253, 22, 8}, {21, 28, 84,
                                                                 120, 127, 152, 262, 285, 231, 238, 275, 409}, {27, 69,
                                                                                                                135,
                                                                                                                164,
                                                                                                                288,
                                                                                                                231, 29,
                                                                                                                208,
                                                                                                                108, 60,
                                                                                                                156,
                                                                                                                275}, {
    44, 72, 123, 248, 277,
    234, 160, 149, 16, 181, 412}, {23, 38, 61, 89, 130, 289, 267,
                                   161, 264, 189, 236, 142}, {23, 31, 38, 89, 283, 130, 141, 189}, {
    19, 107, 115, 124, 269, 193, 230, 270, 226, 172, 170}, {15, 45,
                                                            47, 67, 286, 229, 210, 172, 263, 107}, {12, 15, 67, 107,
                                                                                                    184,
                                                                                                    276, 193, 199, 249,
                                                                                                    17}, {9, 26, 54,
                                                                                                          100, 111, 114,
                                                                                                          168, 174,
                                                                                                          224, 219, 242,
                                                                                                          148, 252,
                                                                                                          294}, {35, 49,
                                                                                                                 71,
                                                                                                                 103,
                                                                                                                 241,
                                                                                                                 165,
                                                                                                                 212,
                                                                                                                 73,
                                                                                                                 233,
                                                                                                                 91}, {
    9, 114, 174, 232, 219, 252, 146, 125, 168, 255}, {
    16, 30, 44, 46, 93, 140, 160, 190, 227, 248, 173, 202, 277}, {73,
                                                                  91, 101, 137, 197, 253, 241, 212, 119, 103}, {59, 79,
                                                                                                                94, 126,
                                                                                                                254,
                                                                                                                167,
                                                                                                                216,
                                                                                                                251,
                                                                                                                136,
                                                                                                                232,
                                                                                                                132,
                                                                                                                223,
                                                                                                                157}, {
    21, 28, 84, 125,
    127, 138, 285, 262, 238, 211, 246}, {2, 5, 32, 36, 56, 95, 182,
                                         176, 257, 13}, {1, 75, 122, 188, 163, 204, 228, 200, 95, 366,
                                                         401}, {51, 52, 88, 121, 178, 250, 214, 238, 125, 124}, {27,
                                                                                                                 288,
                                                                                                                 69,
                                                                                                                 139,
                                                                                                                 208}, {
    6, 57, 68, 126, 136, 223, 251, 247, 191, 151}, {
    19, 25, 52, 63, 109, 121, 124, 205, 276, 17, 115, 178}, {16, 44,
                                                             123, 132, 136, 167, 202, 160, 234, 248, 173, 232}, {16, 44,
                                                                                                                 132,
                                                                                                                 140,
                                                                                                                 149,
                                                                                                                 159,
                                                                                                                 202,
                                                                                                                 248,
                                                                                                                 173,
                                                                                                                 227,
                                                                                                                 234}, {
    61, 80, 97, 130, 141,
    264, 236, 267, 289, 220, 279, 162, 166, 272}, {61, 77, 80, 97,
                                                   161, 166, 279, 220, 236, 185, 348}, {1, 5, 75, 95, 122, 154, 188,
                                                                                        176, 228, 14}, {27, 29, 48, 65,
                                                                                                        69, 113, 135,
                                                                                                        139, 231, 60,
                                                                                                        288,
                                                                                                        287, 217,
                                                                                                        305}, {22, 35,
                                                                                                               49, 66,
                                                                                                               71, 102,
                                                                                                               103, 119,
                                                                                                               133, 147,
                                                                                                               212, 233,
                                                                                                               241, 260,
                                                                                                               336}, {
    42, 77, 80, 97, 162, 279, 220, 236,
    185, 265, 161, 348}, {16, 123, 126, 132, 136, 151, 159, 232, 202,
                          251, 234, 252}, {9, 26, 54, 100, 111, 114, 146, 148, 174, 207,
                                           219, 255, 224, 242, 258, 352}, {3, 20, 66, 74, 85, 179, 195, 196,
                                                                           76, 215, 98, 221, 243}, {48, 110, 226, 230,
                                                                                                    269, 172, 217, 143,
                                                                                                    105, 271, 329}, {8,
                                                                                                                     40,
                                                                                                                     53,
                                                                                                                     55,
                                                                                                                     72,
                                                                                                                     81,
                                                                                                                     86,
                                                                                                                     87,
                                                                                                                     116,
                                                                                                                     187,
                                                                                                                     244,
                                                                                                                     278,
                                                                                                                     201,
                                                                                                                     181}, {
    15, 67, 107, 110, 143, 144, 170, 193, 269, 230,
    229}, {16, 18, 64, 132, 136, 149, 159, 160, 227, 202, 251, 223,
           191}, {9, 114, 146, 148, 168, 219, 255, 258, 252, 207, 232}, {5,
                                                                         7, 75, 99, 128, 194, 239, 284, 221, 259,
                                                                         188}, {5, 13, 32, 36,
                                                                                95, 153, 163, 182, 199, 257, 17, 188,
                                                                                249}, {1, 14, 50, 122, 131,
                                                                                       240, 228, 256, 204, 200, 274}, {
    51, 52, 88, 121, 155, 250, 124,
    109, 214, 158}, {3, 74, 76, 85, 98, 169, 196, 215, 218, 56, 195,
                     243}, {34, 41, 90, 120, 213, 207, 261, 104, 26, 54}, {39, 40, 58,
                                                                           72, 81, 86, 129, 134, 140, 272, 187, 171,
                                                                           116, 277}, {5, 13, 25,
                                                                                       32, 36, 95, 153, 176, 257, 17,
                                                                                       199, 249}, {18, 30, 46, 64, 93,
                                                                                                   209, 190, 227, 210,
                                                                                                   263}, {12, 15, 67,
                                                                                                          107, 145, 276,
                                                                                                          193, 199,
                                                                                                          249, 17,
                                                                                                          225}, {27, 80,
                                                                                                                 97,
                                                                                                                 108,
                                                                                                                 162,
                                                                                                                 166,
                                                                                                                 265,
                                                                                                                 208,
                                                                                                                 273,
                                                                                                                 220,
                                                                                                                 236}, {
    37, 51, 59, 79, 83, 206, 250, 216, 214, 94}, {8, 40, 53,
                                                  55, 72, 81, 86, 87, 116, 171, 181, 278, 244, 201}, {1, 75, 95,
                                                                                                      122, 154, 163, 5,
                                                                                                      175, 176}, {23,
                                                                                                                  38,
                                                                                                                  89,
                                                                                                                  129,
                                                                                                                  130,
                                                                                                                  141,
                                                                                                                  142,
                                                                                                                  267,
                                                                                                                  264,
                                                                                                                  289,
                                                                                                                  55,
                                                                                                                  272,
                                                                                                                  283,
                                                                                                                  375}, {
    18, 30, 45, 46, 47, 93, 149,
    183, 210, 209, 286}, {6, 18, 57, 64, 68, 157, 247, 223, 227, 251,
                          173}, {4, 20, 83, 94, 96, 117, 237, 254, 216, 243}, {12, 15, 19,
                                                                               67, 107, 115, 143, 145, 172, 184, 269}, {
    7, 99, 128, 175, 239,
    284, 259, 221, 76, 389}, {3, 74, 85, 169, 179, 221, 7, 128,
                              76}, {2, 3, 56, 74, 76, 78, 98, 169, 179, 215, 218, 243}, {73,
                                                                                         91, 101, 137, 150, 253, 212,
                                                                                         119, 22, 241}, {24, 82, 118,
                                                                                                         225,
                                                                                                         263, 274, 50,
                                                                                                         67, 209, 14}, {
    12, 13, 17, 32, 145, 176, 182, 184,
    249, 276}, {131, 154, 177, 204, 268, 240, 122, 228, 256, 11,
                1}, {8, 53, 87, 116, 171, 244, 187, 278, 224, 40, 419}, {16, 64,
                                                                         132, 136, 149, 159, 160, 167, 173, 227, 251,
                                                                         223, 248, 407}, {10,
                                                                                          20, 33, 62, 70, 92, 112, 117,
                                                                                          280, 266, 245, 282, 237}, {
    122,
    131, 154, 177, 200, 240, 228, 268, 256, 1}, {17, 25, 63, 78, 109,
                                                 158, 257, 276, 13, 19, 332}, {37, 51, 59, 79, 83, 186, 250, 216,
                                                                               94, 4}, {26, 34, 41, 54, 90, 104, 168,
                                                                                        174, 180, 255, 258, 261,
                                                                                        213, 219}, {27, 69, 108, 135,
                                                                                                    139, 156, 185, 288,
                                                                                                    273, 265, 60,
                                                                                                    29, 287}, {18, 24,
                                                                                                               30, 45,
                                                                                                               46, 93,
                                                                                                               183, 190,
                                                                                                               198, 210,
                                                                                                               263,
                                                                                                               286}, {
    30, 45, 46, 47, 93, 144, 183, 190, 209, 286, 229, 263,
    341}, {28, 125, 127, 152, 246, 285, 238, 258, 255, 262, 214}, {
    22, 35, 49, 71, 73, 91, 101, 102, 103, 119, 133, 147, 150, 165,
    197, 241, 253, 260}, {26, 34, 41, 54, 90, 100, 111, 180, 207,
                          242, 104}, {51, 52, 88, 125, 155, 178, 186, 250, 238, 59, 211}, {
    2, 56, 76, 78, 98, 169, 179, 196, 218, 74, 301}, {4, 37, 59, 79,
                                                      83, 94, 96, 151, 186, 192, 206, 254}, {29, 48, 60, 65, 105, 110,
                                                                                             113, 170, 287, 271, 273,
                                                                                             164, 226, 230, 231}, {2,
                                                                                                                   56,
                                                                                                                   63,
                                                                                                                   76,
                                                                                                                   78,
                                                                                                                   98,
                                                                                                                   179,
                                                                                                                   196,
                                                                                                                   215,
                                                                                                                   257}, {
    9, 104, 114, 125, 146, 148, 168, 174,
    207, 255, 258, 246}, {61, 80, 97, 161, 162, 166, 185, 236, 279,
                          289, 426}, {7, 74, 76, 85, 99, 128, 169, 175, 194, 195, 284, 239,
                                      259, 327}, {11, 62, 70, 112, 131, 268, 282, 245, 33, 266}, {6,
                                                                                                  57, 64, 68, 126, 132,
                                                                                                  136, 151, 157, 173,
                                                                                                  191, 202, 251, 247}, {
    9, 87, 100, 111, 146, 201, 242, 168, 53, 244, 252}, {24, 50, 67,
                                                         82, 118, 198, 263, 274, 14, 184}, {43, 84, 105, 110, 115, 143,
                                                                                            170, 217, 230, 269, 270, 48,
                                                                                            65}, {16, 18, 30, 64, 149,
                                                                                                  160, 173,
                                                                                                  183, 191, 202, 136,
                                                                                                  251, 247}, {1, 14, 50,
                                                                                                              122, 154,
                                                                                                              163, 177,
                                                                                                              200, 204,
                                                                                                              256,
                                                                                                              240}, {45,
                                                                                                                     47,
                                                                                                                     106,
                                                                                                                     110,
                                                                                                                     144,
                                                                                                                     286,
                                                                                                                     235,
                                                                                                                     172,
                                                                                                                     281,
                                                                                                                     210,
                                                                                                                     353}, {
    43, 84, 105, 115, 143, 170, 172, 226, 269, 270, 217,
    110, 364}, {29, 65, 69, 113, 135, 138, 139, 164, 217, 48, 60,
                275}, {123, 148, 151, 167, 252, 132, 9, 159, 114, 174}, {49, 66,
                                                                         71, 102, 133, 147, 165, 35, 103, 260, 296}, {
    44, 123, 140, 159,
    160, 248, 16, 167, 132, 252, 299}, {42, 106, 110, 229, 281, 271,
                                        265, 47, 273, 287}, {61, 80, 97, 141, 161, 162, 166, 185, 220,
                                                             279, 289, 264, 340, 426}, {4, 20, 92, 96, 117, 192, 266,
                                                                                        203}, {
    21, 28, 84, 88, 125, 127, 138, 152, 155, 211, 214, 285, 246,
    337}, {7, 99, 128, 175, 194, 221, 284, 259, 76, 389}, {1, 14, 50,
                                                           82, 118, 122, 177, 200, 204, 228, 256, 274}, {35, 49, 71, 73,
                                                                                                         91, 101, 103,
                                                                                                         147, 150, 165,
                                                                                                         197, 212, 253,
                                                                                                         435}, {26, 41,
                                                                                                                54,
                                                                                                                90, 100,
                                                                                                                111,
                                                                                                                146,
                                                                                                                213,
                                                                                                                224,
                                                                                                                168,
                                                                                                                253}, {
    3, 20, 37, 83, 92, 4,
    169, 179, 192, 196, 307}, {8, 53, 87, 116, 123, 171, 187, 201,
                               224, 40, 278, 81}, {10, 11, 33, 62, 70, 112, 203, 222, 266, 282,
                                                   280, 295, 373}, {28, 104, 114, 125, 127, 152, 211, 219, 238, 285,
                                                                    258, 255, 261, 262}, {6, 57, 64, 68, 157, 191, 223,
                                                                                          251, 136,
                                                                                          227}, {16, 44, 123, 140, 149,
                                                                                                 159, 160, 234, 202, 72,
                                                                                                 429}, {12,
                                                                                                        13, 17, 32, 95,
                                                                                                        145, 184, 199,
                                                                                                        176, 182,
                                                                                                        276}, {51, 52,
                                                                                                               59, 88,
                                                                                                               155, 178,
                                                                                                               186, 206,
                                                                                                               214, 125,
                                                                                                               343}, {6,
                                                                                                                      57,
                                                                                                                      64,
                                                                                                                      68,
                                                                                                                      126,
                                                                                                                      132,
                                                                                                                      136,
                                                                                                                      151,
                                                                                                                      157,
                                                                                                                      167,
                                                                                                                      173,
                                                                                                                      191,
                                                                                                                      202,
                                                                                                                      223,
                                                                                                                      227,
                                                                                                                      247}, {
    9, 123, 148,
    174, 232, 234, 146, 167, 114, 224, 370}, {73, 91, 101, 137, 150,
                                              197, 241, 242, 212, 103, 376}, {4, 37, 59, 79, 94, 96, 126, 151,
                                                                              192, 216, 57}, {104, 114, 148, 168, 174,
                                                                                              207, 211, 219, 246, 258,
                                                                                              261}, {1, 14, 50, 82, 118,
                                                                                                     122, 177, 200, 204,
                                                                                                     228, 240, 274}, {
    2, 13, 17, 25, 32, 36, 56, 63, 78, 153, 176, 182, 205, 218}, {34,
                                                                  104, 114, 174, 207, 211, 219, 246, 255, 261, 168,
                                                                  28}, {99, 128,
                                                                        175, 194, 239, 284, 221, 7}, {22, 102, 119, 133,
                                                                                                      233, 165, 35,
                                                                                                      212, 103}, {28,
                                                                                                                  34,
                                                                                                                  104,
                                                                                                                  120,
                                                                                                                  127,
                                                                                                                  180,
                                                                                                                  207,
                                                                                                                  255,
                                                                                                                  258,
                                                                                                                  262,
                                                                                                                  246,
                                                                                                                  285,
                                                                                                                  275}, {
    28, 104, 120, 127, 138, 152, 211, 261, 285, 275, 246,
    324, 392}, {15, 18, 24, 45, 67, 82, 118, 144, 183, 198, 209,
                225, 210, 30, 286}, {61, 129, 130, 141, 161, 189, 267, 272, 289,
                                     236, 38, 279}, {60, 97, 106, 108, 166, 185, 208, 235, 273, 271,
                                                     287, 29, 281}, {10, 33, 62, 70, 92, 112, 117, 203, 222, 237, 245,
                                                                     280, 282, 328}, {23, 38, 61, 89, 129, 130, 141,
                                                                                      161, 189, 264,
                                                                                      289, 272, 386}, {11, 131, 200,
                                                                                                       204, 222, 282,
                                                                                                       112, 62, 333}, {
    19,
    43, 115, 124, 143, 170, 172, 193, 226, 230, 270}, {21, 43, 84,
                                                       105, 115, 121, 124, 143, 226, 230, 269}, {48, 60, 106, 110, 113,
                                                                                                 170, 217, 235, 265,
                                                                                                 281, 287, 273, 390}, {
    39, 42, 77, 86, 129,
    134, 181, 189, 264, 267, 81, 40, 161}, {27, 29, 48, 60, 65, 106,
                                            108, 113, 185, 208, 217, 235, 265, 271, 287, 281, 288}, {14, 24,
                                                                                                     50, 82, 118, 177,
                                                                                                     198, 225, 240, 256,
                                                                                                     311}, {120, 135,
                                                                                                            262, 138,
                                                                                                            261, 139,
                                                                                                            231, 104}, {
    12, 15, 17, 19, 63, 109, 145, 158, 184,
    199, 205, 249, 13}, {42, 44, 46, 58, 72, 134, 140, 149, 39, 181,
                         290}, {8, 40, 53, 55, 81, 87, 116, 137, 171, 187, 201, 244}, {42,
                                                                                       58, 77, 80, 97, 161, 162, 166,
                                                                                       220, 236, 264}, {10, 20, 33, 70,
                                                                                                        92, 117, 133,
                                                                                                        203, 245, 266,
                                                                                                        112}, {106, 110,
                                                                                                               229, 235,
                                                                                                               265, 271,
                                                                                                               273, 287,
                                                                                                               48,
                                                                                                               60}, {11,
                                                                                                                     33,
                                                                                                                     62,
                                                                                                                     70,
                                                                                                                     112,
                                                                                                                     131,
                                                                                                                     203,
                                                                                                                     222,
                                                                                                                     245,
                                                                                                                     266,
                                                                                                                     268}, {
    23, 31, 38, 89, 142, 130, 189}, {7, 99, 128, 175,
                                     194, 221, 239, 259, 76}, {21, 28, 84, 120, 125, 127, 138, 152,
                                                               211, 238, 246, 261, 262, 104}, {45, 46, 47, 93, 144, 190,
                                                                                               209,
                                                                                               210, 229, 263}, {29, 48,
                                                                                                                60, 65,
                                                                                                                106,
                                                                                                                108,
                                                                                                                113,
                                                                                                                164,
                                                                                                                208,
                                                                                                                217,
                                                                                                                235,
                                                                                                                265,
                                                                                                                271,
                                                                                                                273,
                                                                                                                281,
                                                                                                                384}, {
    27, 69, 108, 135, 139, 156, 164,
    208, 29, 60, 273}, {23, 38, 61, 89, 130, 141, 161, 189, 220, 236,
                        264, 267}, {277}, {309}, {}, {}, {146}, {245, 373}, {233}, {}, {
    317}, {234}, {305}, {215}, {}, {}, {}, {300, 164}, {316}, {
    243}, {403, 422}, {291}, {130, 318, 386}, {274, 118, 316}, {
    320}, {}, {}, {}, {306, 311}, {298}, {310, 130, 386}, {}, {
    312}, {}, {}, {}, {262, 392}, {}, {}, {221}, {266}, {
    170}, {}, {}, {205}, {268}, {}, {}, {165, 377}, {238}, {}, {}, {
    236}, {210, 436}, {440}, {250}, {}, {}, {126, 387}, {}, {162, 97,
                                                             166, 80}, {}, {75}, {}, {168}, {229}, {
    424}, {}, {}, {}, {}, {
    128}, {95}, {}, {}, {}, {230}, {20}, {154, 401}, {}, {68}, {}, {
    252}, {}, {101, 391, 91, 73, 410}, {245, 295}, {}, {189}, {
    253}, {396, 336}, {}, {385}, {100}, {}, {}, {}, {60, 287}, {
    379}, {318, 310, 267}, {346, 126}, {}, {239, 194, 99}, {271}, {
    372, 91, 101, 73, 410}, {262, 324}, {}, {}, {}, {377}, {}, {}, {
    134, 58}, {62}, {366, 154}, {}, {422, 308}, {425}, {15}, {}, {16,
                                                                  202}, {63}, {138}, {101, 372, 391, 91, 73}, {}, {
    140}, {105}, {
    76}, {418, 124}, {94}, {}, {415, 124}, {87, 53, 201}, {96}, {}, {
    403, 308}, {}, {354}, {404}, {236, 220}, {114}, {121}, {
    248}, {}, {}, {}, {}, {}, {241}, {341}, {}, {}, {14}, {
    342}, {}, {}}, $CellContext
`goodPts$$ = CompressedData["
1: eJwVl3k8lG0bhmfMYGZss5tESQtJIpIk90UK8SKUJYS8lghJoiyjlGylKMqS
LSlLtEgISUqEvESyjCUUyRay9T3fX / ObP2Z57vu6zvM4Njh5m / 3L
h8PhyvA4
3
P9f5fS7xhLvC0FrrnOi9wAHrDxemdzW / YuKXs + 9
fR0qDkp + I3Nd14cQkRA9
HDvCAd6vuiHl5mqkYRSQdfUAC2qPPTDT2EsETy / Vr / ElHDho4c2k5rFB8cz1
2
t5bTIDIo7RsmRWEo + 3
KPPO8Hbn0MFTE6CzI1Vsw + SRJBNy / CyK / B0qQQ7x3
ykMrCugLJZkk14nD5LViWUrDF5S2eu3JXDYDcE88qv / x60b5BqMBi7MC0B2J
z90Qy4DxNWo7jNuJcNXfotOLx4IWqb + HY34LQ1LbYea3LjYEpKzd3ZhNhmVv
QvdpNh0 + h6UKZDUy4ajKiMBaXSpc1UgolJoiwiyvP / 6U
OAuuZqu5T + +jw9yz
HWFiJXToHObL9ckiQOb36U9SknSA2ywdkfZ2tPyT62EbygGSU8Wcwt0lxBTu
lw9uEYHuZ3 / uE5E4kHbaZP9izKJDtTZrtLl0cNtRvGswcRZ5GqjtzosTBZ1 /
uxUlTjLB9kWWgSaeD8z0 / 6
HLIRb4BLh9 + 7e9
A4XfzDXT7eSHgGJdBukPAbop
hyrMpXHg6f9NSLh / BnXKRzYInaYATxZ3dZcYEZYnKv1mlATBhn4pvbaPBkSx
7E8
z4zRQr + E6u8 + IQdHGgSukg1OItHn + 7J
V9 / JD5wlhpWykbnvy354b3XTZM
3lU
yUBxrQwG4sRc / sn4gqotzxNleInzev091bO0aUD3QHbWmZx7lVxduCWzg
A / X6S5zuCHHgUaqXhiKH0FCaaVMTsKDN7VPTYjgNpM0 + JFn3LaAymdWdPbdo
MKv0SzfqqgDg8oVyiA8Z4BZJjj55gR + oZYP8YkeHEJV8M87Tlg8sJA5n728Q
A8ipTyxWIEGj9cxYyGEc2MY / lPWcFgXTfG3NPg8GvBfhPmjcIwLUZC3Xmk5R
UOr / Oex0jAqParfI6DjSgLqvJXllQQzcbJ3jrBJFIWAWP / mqQAQ2nfY15 / KI
oBSokhG / iQw8IaGd + SK9aIhb3mAM88i56R / FMyfEgH1dTToF2EBUP + chaDGN
dNkPNBdV6VC0o6dT8ewfpNG + Mnn2OB2camt9jwyyIFws9sctNj9MvtV2D / Hu
RLDj8rbTTAGYrSg9HibPBFyOtVD5LB5GU + 5
Xu7JWkURabskenjiEJJXxjbxh
Q1rM2nczLQwIeO404RZBBVy5Wck / DDL4iCk1rah2I82Xd + KSXtBBfyexOO0U
P5CUU + VxCwKg8F6tf / mdCChFnR4 / ILWKuI036tT0WIBru993piECLah2RO2n
42
Hcyzw1FMcCErob4XqDAZlbpEJx / AxIuJGsd / 4
EATitq9G3e0iA0znjyWge
QqYT1y / yW46jZdGLe25EU2B83mV8QJGO7aum82QEG3Z26n0qCGGCQ5tU2m51
AgSkDkkpRxNgyOoU7ewiC5Rym1xnpf9D6R1xYBfRgjzvf1V + cnsRJdxxpbqu
Y0DcJx1Hw5sk8B848mehTxwcJs6Kjv63hGpvtH0xD5xHDscvHOw3bEV + U8U3
fgkKQJH8Tr + H1zsQt3Ro / uH8EsLduYobVy9AcpLRUq + MxcCZ8CTFPUwAfELm
+ k5uW0S6ViyHo09YwCvRtZO9VYtMNd7NWzfTQVrDfqp9UgiMUsSZYy18oJUn
UGeRyABn20veZEUixBHy51X + EwUzh7LAQWwfOVufm2i5DCBdy88Ba61ZUKT8
86
d22QpKv2XT0OIiAra4yN0qgzMojh5Y97xpEFm5txNKn9Kh + xrqW + byg9f +
6J
VAEhtKLU9 + TftOBNLVtoZS / Bwyk / Dz3 / ebCqPCkCUpSYMYTaMdN0mziCqE
ritl81DMbnrIKSx32gY2CrQ / EYfsp34CQtpLqLpq7tI95yLEfaWqJ6OZi7wK
62
S3k2lw + 9
fEkDWWZ + l89BBP7xpk1hm7VCTBBKXF0p7Bw4JQqkattRHiQOVP
S + jo5kDKHUty5gwTNFfVB4ekhcEza / e9DQkECHK4vVyfvoj010uyf4pjeX83
5
vqrTQSwKrxh45E9grjDS + l7a14j6XoxcthdIvA + vMb3nhOHirZoa1GXRaSw
6L
6
yKr4GhoRULaa1JhFu8tPE / U33kU8eI + Wv8h + U9PRKQKb + OPIZNVhbuoEE
6
W8a5zo88CB585Xnuw3C8Cwgo07lPgVyK3q1Pf6QwU0Z57ffWRAKs / yqD6TS
AHfsrIbiWgGQ9D2y3v8EEbhbaOs52njYUti0G + kxQP0S6061HQl0M9fJHsWe
ixt + o3 / SIx2NCukhl3l + KOt9ItMRi81FVMKAVsgHJBes8zV0kgC693NFlN + S
gDqlZ7fVoAttCu9 + / j1bGGJSatav9SVAy0Oy65g0DfjkNYP4VFkw5OZ3tvwc
P / iY + R7KPC0OtR / rU8 / +EAf1LRPq7i + oUAu8EaWTLKDu2lZWjJ2755z99Yj4
ORRuOHrR0HsecSdTNu7O5IcFwe / T / WgFZe4MWYOPpIGVbPMoDAoD7qmDmeXG
NJRwr8fxxik2jH578W7LHmEgtqTUOcngoGR1Mkb0Hxq4URzHR0MnEIdhf8xM
DuuV1RwtLSdxKDok1BFqSwfJrrIkeDWLoGBL88xZCoxSrF4p7l9BpZVNEzVz
35
G0vwvFcjMdFCrJZHEFAugY1YfqvqGBz7tG + cCoZXSwcuX9Gjk6TH7zDj + g
9
RnV6Gkkb9 / OhtylCiu7ciosPjoVKVfOgdKbAscPNY0j9rtrX9TuUaHz0NQQ
rgTLr + yIuXGjv2jUn1ooacMHlQZJ3ZpTLKhrIlx4 / ZkGOZUjj / ueYrmkbes1
aLqCuJrDTlZmi6hRRzJrazwZZmPKNKOx / NLcMNrffYAI + cdY7O8NDIh585GU
EiQETM3kk5KGVODgNpzT6llCLQ / OKVPbaRi3bHCvfzSFxrfZJstvw / Z67ukd
l3oqcJUj49xPCIPt0smo0BoqOPCOV80kk4AUJRy + sh / jDOo3w6bIl8hB + m9e
WRc2Dxlqn + cTWxBX0X4moRbLHYld2iGnWlCp1zaDkC2i4LXxldyuVSwXj21x
rmgWg5pLFcF3SOLQ4pN37eniKgrKcNNNt + GAhu6mf2SxXi6dMH7gdGYOxX1t
KRz + TgGuRs5pchsfwL0j4d9GxSHBUfoQQUsITPdsvtJB6Ua5Q619gug3inmI
yt4fp8HVC35eYUp8WJ / PBX / WXEY2l2yKla3YoC8vbe3jy4BRuzXjvFg8OP3h
M + n7lwHGdZT / 2
O9YENC2bGQ6KAaPWAv8YzpMKBUq7 / rvkxhILiXYMcewvlUZ
Pn7LFQ / cWHOnpiPY + fxILH + C5U / uLRd0ZDcZmqpEYs8scGDyR9 / QRBceHNwV
bE1TBAByY899yniBkgKT3RpvziHOnSjBoSkhqF6psO09QgRTM2vT8UqMM2iy
ucKWVIBjqTY1Y82IG + nuaGJPAvWLJZTlE1MoffokX5jBWxRQWXcj + Qc / KASr
vcgMFQEOS9To739M6CTbudak8YOucpS9iAYJ7M8j0UWs75X8d901cWVCUJ52
xsBZGhRNeRSQf7YgfZkO4qFJClgtbc7afYkPcL282yl3vqDwCg176SP8UDRa
r8GQwHL1ufkFkxIxyH3tdNhyIwcs / DcveY / MIwWpkTULZRi3Pc68kG04i9jz
zQneaRxwG1Ylzd8fQzEquys39BJgTjW1 / 2
Ilxol2lWodlgKQn6UeLBhDBKc +
X86SDMaBsuLlVj00yG5Rg / V8dFAadXPmPiSBgI9U5IoZA4K6KdoBH0mQpPv1
mvYb7H / 6
nGzemzSKcEkFC04mDPjQpOtwwZ0JxPguqWVRfghKxdfveUUCaenf
B11FmtDcpkO3D7jQgXqinSEUu4LCBX7xPPVo0FWgLbkvlAoCt6tMGg8ygW9E
/ 9 / zbxnAyW8t0XnAgcbLkWsrGlhQsZgbXHdaAORet0iL + NAg9 / 2
Y0cw6Pux9
vsw2 / UGU8rnn9ppdM8hNYrAzd5CHhgrlItdGzqEPBx + 1
v + JwoGhFU / nXGazf
4u
8
eUNmzgnTPC7xc7yQKClxNrUgiE9r + 4
HrfygmC26zVlUsh2Bwe2PSCjO1h
tbPOaRehRlTXaJxlp8yG9G6BI / LeGO9KtBwS + cGEEvIUX8UsFepCtkZv7RAH
Ln0JiexvQAkHXEmFQRgfpa8zn3tdjZ7VCe9xD8NDpkmizJZgJsg1O1T + XP8D
8
bbXhApKMmHh7MWqvitDqDpSbKhSRxCIJi0tOVXY7 / BldWklEyCm9 / O1bzwq
dGUU3pPopEG + SJeG4FYqGIVY + xxPpILCx3fbHolPIQuKY4GmrTAcfRZsfduF
A6YRz3Yqpi6g9Kn0PRNKg4hL8BL27SYA7qHeQL3mBKr1t / jCmqCCXGrBg82N
GAfP94gdzxaH6rjnI4nv65FPgcrxjlAGpMhNp7cXEKGTcKJ / MpAM7 / +MNpdf
WUK5445EkSk2SJ9Ls37dwEMJDVH454MUkLa0mpe9JAzCmoHmCrZ40L9xQ7ni
8j
IqykwL6H7wFbXSd4Q8mWfA5LtdumUz3Uj0tO2FFWE2xF1wmUl7TYe7E4nH
2
ikcUH / OMBs1FIShnrszkcMioE6ujdupgfHc4M + M8CHsOXY + CIu5LAIhvlwL
OnaPNoUhvsfiaSCc1x / s4ikKV9e + Zb4X48D70u + pKlieDlUd7ng3LgK5K54S
wXxEWDhTlUhWE4U4TsZBaiEO2ja2NF9hC8J0w3PalBEH5Pq + kJ / 2
iAKEBxhv
z + 1
ADu3M + V3V0yguJsKrKIEFuqeemCRVCkO1hYmx42sKzA5dxz0VowDOGI2V
nxOBID1RWmcolkP8ZpL4JXGQxyeXS3WwgeQ5bkgc + 42
IXr2ltB4RyB5Rviux
gw / Sg0vvHY4YQpl + M / QiBey + P + 5
VqHglDnNd / 13
s / cWBXIL11SsfME + 9 + Hdp
TC4Z1VIsA2U / ECHgXcLh + vx + RO9vvHK0QBzM3ko613Cx / keiOQbjArCYuvA3
2
gfzp / uP3cae9CKroxkJM / y / 0
Puh / LfDuUKQkDsyF / uUCV5XJIq2zDLAM9Dg
4
mA4xmWEx2dEyCJQmpVBq5IkwcGHble + p2Hcfve4gLL9L / RosHbPdwE6HJyz
/ 0
wTwPKzy8C8yZ4OSVFpdnRZDmxKEfr9MlcYEpYJty7PiEN6pH1rbBUO86vW
wKi + R2iWEbA + Xp8Bpmf8T54hD6Oi7Tn39C + QgWuYlxbqKwqHHse + wQeIg / S7
r7N92nzwAx9xyGYS6 + Ez / 5
C3po4gi5jwKpojGZ45Fj8qPYmHyffHD1dSJ5GF
r4NG936MC9eN6CtH / 0L
6
PSXZgkITqGhtf4 / jN0EwNd6ncZHvN7LS6KqNjsN6
lUMrcnYRAyeP6Ie3PtJBcbv7hbyNNKjYO1rt5YQHI + noRSJPEJTCDwjeec0P
voWSpCtNbIAkki5j52vkckLR7yybBpN76gwNDuHgyl65Lu3ndOBFrhQ7N35G
o85argZsIpbfxx2ThahgayL089IKDuJa1z / uEMVyXdZ6xmRVEFQ1skcPrpDA
oXm1NLQU81GnnseGvwngV7y1wPQ75lGJT1 / 7
bxQA5qbgp8bZWK / cZj6LusoC
q + ST8jw0j5j2We8GEzFv7DNKinDnBzXLStNTOQywEbQqHl2hge2RQ5X97ljv
bVL7kveJCUVhAl9OSxLAZ2c7nSiEzXn / ShO / CRE8uTO2EcCBah0f3vCdVpSw
bVerOJMCKRu1psqPk + Fi9UP5hm0s7J5kk7LnmtA1A1NvN36sNyquFWmvnULC
OmVPWpXw4Na2bjmd8A1lv / qWsPBhFk2qvqycTqZAzI + J3CaeKPCkDgqffykG
ngm / iB2u / JA + b / HVgUyCcJmjlzc8xXzNvCGixIwAw17Me6pKVNDvfkc0Sl1B
ZeQDNb3VNPCb / 0
R1DheCZYZu8Zd9LDhUYFZ6PI8GsDlHhqLFD + pzIXt7fDkw
dD10 // zQDEpxKswejsRy + lmaXP6N50gpUIr1NYkEbtpX7wirY / lTNXLxTs1X
RJUz / Ru9sxfVEnUGZNbMINOhCouwDGxuLAqJB1LwgDuy1 + vWBQbonEsrwz / m
wPQOjd3WPixwc / TKTDEWhoXOS7h1M3gIilY5Z21Bguzabkod9w9S + LxPnqYs
Drc7n1C3FXOguypQ9RBFFJ7Z31v + cQXL3eQk9s3NmDc4ZxRdd51BmmUx1WY1
QjCpEn / Haj8fVOi77608LwhgxJ28 / YgG9PwexSs4bA6lOLw58z7UK73tmIQE
B8CtVzvgJwVKbym5t7VSocxSRWnpGgtW / TcvBJlifhKR / TrEH + PnkvxTgoXL
yJczc2xdKXa + yusXXcJZkC4URCFzP6Iizevtgxsm0LhE0ciIAhNME + aj7n / 8
i7qF93P8sT63P + N3rusWGz4ET03OV4hD25ePNVHpBGALD65JVqNB7x + fKl2M
63
xuvNmklsyA3Jr + hzOjHND0UZT7lUuDhWSP8NScFSRdRmLiMe + Ujq78mPhv
I / LprlL5Q / +MpB1m236dnEBR6mPxRf / nZ82N5XY5CyiggKZSuHEA + bdGbkjJ
ZgKv + Wmb9YVm5NzK3b74CA + mDd6Z3X9m0WzJsnuyKhlKMu86HBJlAKw1mH / V
gj2 / auBL5TA6eP6tXCYqkqDzveBwxsAScnN / 2e430
o98PrSN2WC8yu3NedR8
uw6VWp2z + B3ND5N7R9YqvcF6KLyWT194DaQvXZe + / +ITotZU5C7cw3LthqRz
tVQxArz + VsIC1nsWMulm + 5
hw95PEhGk9HUC2aOt + nza0XJl6 + sNOPji // J4m
iPV69UOFZVOXKiSsp3f / 8
wL2PT4fyPi6OLTJIvF8g8dvJDcQkhF8bR6pvywO
SyOLAmnAMPRDPBtMj8mqjb8Sgdou7fh1llNI6bvs771l35Bn7sfbR6VFIZ / p
0
VFKw0Mcbq0HJUsM + F7a7Xb7QwUfvcozG4KXUbcAx0fBHcuV8RerBrJTKN8p
va + njAY / IFfX6AALugtSDfuWyRD0ZkAgpYkG0o7x / 1
TdYkLCZfP1jfrioHm6
+ I55NR1OrqtSHPRnAofoeLHMbwUR8zQ6 / TQwT9Z1e1hSQgALxiF1OzsitPXU
XcpTY0C3zomdkV8wLs + QT9HT7kGlmiMpX5PFoDNojbQeiAMct2Ox77SgRsPf
1L
QFEvC88HFjhUKgPmDAlNEVAdFS3rNhLex + pEMq9lwgQO01o1TmSQrIv3DW
O / OAAXWD7frn5DkwkLDbcTQK43K3Funuz8sofbPbvdBfLDCVkLK7i / V1eGh9
bH + MAHB091Dvza2i9PrEtjaTEcRLDRZUx3jT4WYSn + E6jLfZProqizgYogpu
0 + qZRqZxSwc + BoiBlquiiVIeA5Qurpn8WioMbvctVD3PYJ / 76
fzVw48A3XPX
+ hSExCBdoyHC80Qjoo5Wm20w50Dt1znecCkFlM5 / ClfoaUdylsP39vV9Q5Jn
JYntL0VAM1jH + 7
YeG5pOnTbo38gESvzUrqCtNGiS6VHA5XPAzFeDcmJaHCan
1
XMff8Q8 / GIPwfvCJeR5att0eDGWP8 + PiLWdxfbx1 / e4 / 8
IXkRYwgtrN2VD0
JkVHUL0PcbfE2meFNCKJtw + bRhAdcg47yBsfpIP + sdFg / scriOQUnhpphXlU
S4bKoh0eOIJhNwI7sT5 / MZPkoj2L3tvEZv4XRQQj2xBrvTAiCLMfXNKyo4N /
eMMR78tMSD / a9JFsVY / ctsf + W4 / x5rMm8XHucSK8f2i5Zncj5sMKB + fz3lHA
mef65lcOEbjlg8p1N8VA9x4x5K4KARzk4szcCvkhrnx1JMZDEM5vclvv14L5
y73k7a2YZ / RuHY50taRBOrFUuStnFVVY + tzhw / KnMJ5nGJSH7ZnY / S9y1l3o
EU5g + LcHEyqCNFXr6jFvMT5bcFNjCCWEPAucfk8CKNLFPQgnQ5zWzwOyaVj +
ys703VtdRPlR67V / n5hFpjGFqz8cSRBlu2s1u1gcGs9bZlBCME4b3Hz5choF
5
ETePo0zJ2F8tOSRojSNSoPXx4USREGDcz / DvxnjzjcsWXLQDOKV5zsnPphA
DjGKXw / Ht6HFPQ5yHelsqOYIOCgb / 0
FFYt91qElUCPe8LvHBnwxDHxPSk7E +
wxk + P9z88wGaNPqUsIzHeiBwxS5 / Zw8Kv // LKFBvDjkNPi6PlloDfk / Mel7f
ooBWp / fvUOxc8o + pujorEWCxTy7UmMSCSZef5ma5mL8daYGqPzTgXj9us3Gk
HYG0sLODVxlymhH6rTzNhFzfp + liblSwuk3PzErHYfNda7lvBONA20 + zwUp /
UErqcBuypoBqWFnk4GVx6LxVRJw + t4jiFq2ipGOxvrLtHzWnYb2orCTRiHlD
nJzpdMx1bM985CKsW / CgMDbRZrxLCKQryh990VtG1d6X7Ti7X6Dc4j9V5Dwc
WFTrE1oVsP + XjhQMj71BE5XdyQIsJizX + EjKXaaBb51IzaZpBjzzL2Dbs / Bg
25
rizdahgZxztfetDWzArQ / LOfOSCGqdNF5mCAeSdCQvPN + BcfDPW + XvFETA
tkTqCStPDOJecw1f7hSCGPXsLIfvVOi0d5bsLZpDuBJpLd / 8U
WSr9equcg4b
RjsTPLPXECD / 5
ieVyQ8EyHbZ0TL5jQkBzTKDcpIiILk9NnKyAw8 + +QX3Njn2
Id63c3Vlg8KQtMVrfRZzGbklMiQ9MB / Jn / Z / Qz3ABPXPXXDQXAQCHnRINST /
RjdtT8jp6FHh6tfvorcal1BrSWlwGYMBmn8Hw0TNFtA6E + OsD1U04BsyGCya
pwOuCtU7xGCep8L0K / gwjSbZ59xPXSACLu6SvY2NA4rbMWBQKbOMHOIXO21i
xMBUxpW1Txbzoc2nlRipotCyI + yVxNQAqp647qa1woGLX7QFPw5jnjW5N2 / I
RRg6H3pW2kmJQ3gld + aZC + Z3uSkixHIBqK688P4xZx7BzozV + QxhqOx9GvYc
myt5S91Neg1M + B / 00
Rew

"], $CellContext`path$$ = -1, $CellContext`polyN$$ =
4, $CellContext
`polys$$ = {{{6.154851328821027,
              5.2251557772383155`}, {5.288825925036589, 6.7251557772383155`}, {
                 4.42280052125215, 5.2251557772383155`}}, {{1.8672715427914282`,
            0.8224405564021584}, {2.2305428067941087
`,
1.9404745451520533
`}, {1.279486290498955, 2.631457550777106}, {
    0.3284297742038015, 1.9404745451520533`}, {0.6917010382064819,
                                               0.8224405564021584}}, {{6.150545055924135, 0.5304448311994676}, {
    5.284519652139696, 2.0304448311994676`}, {4.418494248355258,
                                              0.5304448311994676}}, {{3.7023812217607563
`,
0.45940127793967456
`}, {4.065652485763437,
     1.5774352666895695`}, {3.114595969468283, 2.268418272314622}, {
    2.1635394531731293
`, 1.5774352666895695
`}, {2.5268107171758096
`,
0.45940127793967456
`}}}, $CellContext
`polySides$$ = {3, 5, 3,
                5}, $CellContext
`polyXY$$ = {{5.288825925036589,
              5.7251557772383155`}, {1.279486290498955, 1.6314575507771059`}, {
                 5.284519652139696, 1.0304448311994676`}, {3.114595969468283,
                                                           1.268418272314622}}, $CellContext
`progress$$ =
0, $CellContext
`pts$$ = CompressedData["
1: eJwVmHk4lG8bhmcYzFhnn0mUtJAkopLkuUlZfxEqRCFZIlsqla1S1koRsmUt
RaIkISSJCBWRLGMJZV / H3vd + / 5j
DcRjeuZ / 7u
a7ztMHO3eQMDw6H24J9 + f + r
rG77cGymEHzLso9172WDrNpMvcOpPjTS3FeiOTqPzF3eGcVo / 0
N57 + c + vg9g
gaL34Fz73X5E4A0fuD3IBs54db9SYwVSM / RJDznIgKoTT0zU9hHA1U3lV1Qh
Gw6ZudPJ2UxQOH + 3
qusBHaxCzAmRvgxI + / W7p8efBRB6jJIhvYJwlF1p51 + 3
IIdOmrIYlQFZOvNGXyUIgDszLzLbW4hsotwTn5oLgq5QnFFCNQsm7uTLCNb9
RMmrd17OZdAA99Kl4j / vDpSjN + SzOMMPHaH4rA23aTCyZveOwy0ECLlo1ubG
YUCT5L8jEbPCENd8hP67nQk + iWv31GeQYNmdt8OTSYUf15L40 + vpcEx5kH + t
NhlC1KJzJScJMMPpiTrHYkBIxm7nqf1UmCvYcU2skAptAzxZHum8kPZn6quk
BBUghqEl0tKClkcDXawC2CB623rP0TAWhIkTHLqACUS70jn5 + CVEF + 6
R82sS
gY6ChUwCYgFxp2XGOG0G0U9PhltKC0NkleEZmeR + pF9luUYzkApOO / J39cXO
IEUD0ZFo21FU8Stgb4fXKHLV270nO1IUtM50KIifxeb7Jl1PHc8DJrr / UWUR
Azx8nH6faWlFQfezTLTb + MAnX5tGXOCFDkH9UlMpHLhe / C0k3DON2uRC64Q8
BYEjgwvZJUaA5bEy72lFAbCk3kip6qYAQSzj6 / QIBVQrA + 2
dp8Ugb2PvLeKh
SUTczL1waz8fpL05rLitiAkvv + +95
x7PhIl4RT2F4Wbkgxt + 8
zf9LyI72Adf
6
CLAjwP7VYbXrgGVgx1hazq5KKcid8vlOh5Qrb3B7ghmAUewYqk / tB / 1J
xs3
NAADzAv9NvoOTCDhI / 56
aoZ4aHb62rAYRAEpk89xFt3ziMP55GbON43y / FpI
7
m9HUbH06s7OBxSYURzXDgvhh4r0cyXzBBY0hzGflcazAJcj9JjwlAZOoaTw
s1f5gFzcxyd2rB + RSfcjXa14wEz8SMaBOjGAx7Wx + fJEyAnyCPn + mgH1TYV +
7
xbpUG8xPex / BAdWUU9lXKdEwThHU73bhQY1IoFP6veKADlBw7GyTRQUe0YH
7E6
Q4VnVFmktWwqQ9zclrMyLwTOzZ9yF / UzwKvpYnNnEBicr + 0j
zWFHwmcFP
vHsuAps8vUwDOQRQvKycGrWJBBwhoZ05Il2oP7Ck7jBwkX3DfwrnT4sB8 + 5u
qURsnwiql1wEzKaQNvOJ + qIKFfJ2dLYpXFhAai0rExdOUcGuqsrraB8DgsRu
/ 33
A5IOJj5rO / u5tCHbc3OZJ54eZ0qJT1 + TogHtsIVQyg4ehxMwKR8YqEk / O
KtzLYYF / XDHP4AcmJEes / TTdRAOf13ZjTsFkwJWYFP5HI4GHmGLDikoHUn / 7
MDLuDRV0dxLyk8 / xAVEpSQ43zw / yNbt7lj + JgGKY58hByVUUWH + vercOA3DN
md3n64LRvEpr2AEqHkbcTJMCcAwgovhgx3s0SNsiGYDjo0H0vQSdK6d5gf1t
NTymkwg4rfOutMZ + ZDx29zrf8RG0LHp9771wQRjhOoz0KlCxvFC3nwhmws42
na / P / elg0yyZvEeVF3yS + iWVwnmh3 / wc5cIiAxSzGhxnpL6jlNZIsA5uQq6Z
v5Rexiyi6IeOZMd1NIj8qmVrcJ8IHoTBzm4jJqzWcLqnfzDgYu / RhfluFtiM
XRAd + r6Equ41 / zS9zEU2p64e6jH4hrwn8 + +NC / BDntxO76d3W1FgUT / 3
KXcJ
4
R6G4EZUnyNZiXDJd4fFwJ73ZaLzNX6gr4hdeM87h9RjCGe23 + MBD / +57
rPb
FpG2OcPm2EsGcAq1rWUeVCFjtU9ci0YqdIQYcEel6KBYpOcbf70HSamdnGyZ
EALDRBZ9uIkHNLL5q81iaWBvdcOdpECASN4crvJ3UTCxKb7ch + UBe + trIw2H
XqR9 / IfPWgsG1Hw9tp7eNo1SPLg / F03GUJ7S6Khm8QpKeWBZ1 + QgAla40D3K
fdMoknq5 + nVDHzJ3buEteoU9xx3UvRzIB24HwlcuE5lQdPzsr + Q / BKixHurp
K1tEI4e2ekqfxQExpLmuCD + HTMS9L + 6
fJcOQMKRLSFAgQt1wx33iDCILobuK
GRwUsYfqfw7L0bwPtRIzR2ig + 3
NmzC / +L2ru3cjf8pIFGa + 8 + YU0l1BF + dyN
R / Z5KPCdio60ehZyy62W2U6iQMz4WL8FltcpPFR / V / dKZNJ2eylPHJvTYlFn
3
xEBKNpNrrIUYkPBnbbDrH80SGGXx6zuZUPZ6HFo7WBD4sPjpLRpOqivqvb1
SwmDa / qeRxuiecHXJma5NmUR6a6XYI6ysL6Lj7j7bhMvmOfes3TJGESBA0sp
+ yrfI6laMdK1eAJwPr / Hd11iQWlzuIWowyKSX3ReWWWtgX4hFbMpjQmEm / g6
lrkpE3lk0xL / KS0g1ZSqpQhJPphXz9XpbhxFkX8Fb4mcEwGfLX7ynnXDKO7V
LZ803RHkMaS3tmgDEVI + 1
M + 1u
uBB4v47108bhKHAJ7VaOVMQskq7NF0WSOCk
hPM + YC8AueneFQeTKIA7cUFNYS0 / SHgdXX / xNAEKxDXsnuTzgeoLgvmD2hkU
uIWynq2Jhy25DXuQDg1UbzAeVlgTQTttncwxbA4 + uy4s1BVyUQih8IkgdwqZ
+ / os1MwzwIdRcaD7 / RgKDLrXM + GSgoaEdJADlw + Ku15Kt97G9jYsulfD / zOS
9
dP6FTDBC9qZWSJKH4lAntSx3qrXjjYFdbz + kyEMEYmV69d68ULTU5LjsBQF
eOTUfXlUGNDv5H2h5BIfeJh46ad5sqDqS23Shb8sUN0ypur8hgxVwBlUPMuA
DCOB3D9fhAFXNufXpDGJyLu2Fedj5 + w6d / JucNQcCjIYum7gzkWBE4kb96Rh
cxb4M9WDVlDaTv81 + FCsJ2p8efWmp9DM67sKMWewc5VpHII + 7
Pe9sjE5vjEZ
1
e / oSorfKQyqXTGJW1VXUfSjTtt755gw9PvNpy17sfk7llsLp2Dn / ptj1RE0
hghNidV20jgoXJ2IEP2PAk6CtiNDAWOITTt5wkQW6 + nVxxoadizI0xdqDbCi
gkR7cRy8m0HwfEvj9AVBKKgf3 / 93
cRLF5VPxWnx4MH7koHRlcAnJvy002sXF
wZCg + TuFAyuoqKxhrHLuD5K66CB4fDMV5MtIJJY8L2gZ1gZof6CAx6d6ucth
y + gz58KdIBwTUtIJslyPGXSobKVmjSwVJn67Bx3U + IEqddQStm9nQtZSqbl1
CRlU / n4P5HGeQHmmk + 8
Ch1dRc5X0NDuXBE1fPUWsCkbQ4rNzobIlbCi6z39K
v2EEMT / d + bn7ERna9Cf7cYVYH2QEz40Y / kNDF8m5EpY8UKYX16E + yYDqBt6r
739
Q4HHZ4IvuV1jOa1q59RmvoED1ATtzk0VUryWRvjWKBDMRxerhWB + obxjq
6
ThIgCYI3WBWsIS83S4dTlueRjknGMw / dTSI + PCFmOgrBHT1hLMSBmRg4zZc
0u
hcQk1PLimRWygYp25wrn02icJ + yu15kkaDZnNS81sKE0a2WSXIbcNyce7V
Q4daMgQqhUY6nxYGq6WzYQGVZKguHclLMMXOZ9ut / T8EepEN51T5dAIRiGHC
QSsHMM4k / zZoCH2LbKT + ZRe3Y / ucuvsHN7YJBSqcnI6uwnJefJem / 7
kmVOS2
Tc9 / iyi4bXwnu2sV66UTW + xLG8Wg8kap30MiC5o8su + 8
WlxFvqlO2imWbFDT
3
vSfDMZZRWOHn9idn0ORv5pyB / 4
IQqDaY09SMw / Ao6NBv4dYEG0rpc + rIQTG
ezffahXsQFn937oF0CyKeIqKa05RIFHxxaY0Axp8cw58eb + NCSFXvd2uKfJg
vDbn90N9GVnesMxXMmeCrpyUhYcXDfSdA97l78a4aKNc9MmhSTRkvWaEcxsP
dgs8Rt1naHC4WvA78xN235uXDY37MH5hzPMNa9GhSKik / ftXMZBYiramD2O8
pDxw6oEjHgJvm9o1HMXm + Te25CWW50Vc3xN4PB + 0
ZXg03X4xgoyVyVk3 + 8
YR
jF11S6fMoawHDujoHhI0lIvcPj / Phom / 3
f1j7XiwcZa3Mk7kB8i6felr6hsU
dznBqf7 + HGI / DBPonxSCipVSq66jBDA2sTAeKcO4kyKTJXycDHAiybJyuBEF
hjrbGp0kgur1QsHl05MoZeoszzW9j8inrPpewl8 + kPfb / SYtQATYDFHDf9 / p
0
EaydqxM5gNtpbCTImpEOHkFiS5i / KZ4cVe8kSMdfLM1U3svUCBv0uU5abQJ
6U
q3EvQnBMF8aXP6nhs8gOvixCQ + / ImCStVOSh3lg7yhWjWaOHbOwcHfF16u
oIyMrv / Y + xZRxmvTq0aFYpD13u7I8Y1sMLu4ecl9kIvkJQfXzBdjnP8i7WqG
wQxichuj3ZMxPhxQIXIzh1GE8p6yDV28MKeS1HO9DPMO67Ldrcf5ISdd1U8g
ggB23V7sJWnMI2RYJeadFMho2g3reaigOORkH / iUCPwekqErJjTw7RDU9PlC
hDjtX3c0P2DP7XG2cV / cEMLFPZ + 3
M6LB5wZtm6vOdCBEtUsui / JBRILsZc8H
JNh0wcHxoOME8k3C1 + 59
RwQpqdlDjiINaG6TfsxBByqQT7fQhG6voCD + cY6r
DgXan2tK7A8gQ4HI0PvKFyRI2Vze1hzxB / HHlBvVH6IDz6DumSsfsZ4PuXUg
PJ0Acfwxg81iM4id861Q6wkb6m + Gri2tY0DpYpZftSc / yL5vkhLxoEBWzbDh
9
Doe7Psc6W26fSjxR2fMml3TyEm8ry2rj4P6c2VD14bOoc + HnrW8Y7NB5fdn
BeHXLAjJ + 1
ASJduL8lbUlcbPY7wSFX9Qee8KkruQQ9ZZwwLzRMmLyW9GkPYV
/ rfr7URBPlBdI5RAh0hfn4OhZGxfb9RFn4udQs0LuK6PsgLgNGN + 64
Y / di8O
bnpDwnKkwl7L00GoHlXXH063VsLytoP / qJw75lviTfoif + lQSJrkKZ0hQ1CS
VtiXaAHob7B6O / Z + BlX7bw3f2sqCQOoSEjlQh6IPOhJzfTG + TllnOve + AhVU
C + 91
voaHNKNY6S1 + dJBttCkbXf8XcbZXBghI0GH + wvXy7lv9qCJUrL9MSwAI
Rk1Nj8uxv8uT3q6RwAsRXT / u / OaQoT0195F4G5aLn2 / s + pAiCm0LTNtScyxP
RdrVBLaSwdDfwuNULBnkv3za9ow1icwEbZ + rWwnDsQI / ixgHNhgHF + xUSJpH
KZMpe8cU + 1
Agr5uwVwcv4J7q9Naqj6Gqi2Y / GWNkkE16 / mRz / Twq5naKncpg
QUXk68HYmlrk8Vz5VGsADRJlp1JanhOgjfd0z8RlEtQsDDWW3FpCWSO2BJFJ
JkhdSrZ4X8dB0XVh + Nd9giB13Jwrc0MYhNUvm8pb4UH33j2l0pvLKC8t2afj
yS / 0j
brD / yWXBhOfdmkXT3cgUU + rqyvCTIi86jCd / J4K8WOxJ1oE2aD6mmYy
ZIDNvTN + OnRABFRJVZE71TA / 6
BtNDerHPsfOJ9ciboqAv1egGRU7d8tcf68T
URQQzu7xc3AVhZC1H + k1YmyoKfqTpIz1RX / 5
kdZPIyIYh9CvpqYJgsQ9E + Pc
mVmUteIq7sdDgPnz5bGk3aIQyU49RM7FQfPGpsZbTAGYqntNmTRkg2z3T9Kr
TlGAIJ / D27NakU0LnburYgpFRgS75UUzQPvcS6O4MmGoMDM6bPteEGb67 + Je
iQlCxwdGRxnmc4pfrxv2e88g3GE0XHJJBHx1RCltAZgfCwkGRMSJQEjqN29W
0
hKy4TORwC + xQA6fUCLZygSi64gBYXgWEdy6iiidIqD + NkbL0YGLCN1mR21n
eUDeNPrcizNMCOqmt / IfnEYZg0rx4jt4IMWv6NGR4H6ky5ZsW1D7hxLLp7bw
XJpGad7T1Dx5bL + +7J
MvfYfxWWNWZtSl36hqz + FwFxwe5tq / X + 8
aZ0MWr0XI
rc8rCHf939KwbAKqEjx + WeYzAXw + RR + pzelB1J76W8eesyDyzsFtHx + JwVAV
cfOJz / PI5KOEfWUgxoNI9LHeCD / 0
q6s0nv26iNQ9bb9LbuSBxaT5f + EeTJjI
fOE0 / LILNT9W37 + GIgLACg9aGz2LzI + lRk / zjaOa / pyPA1lCEJ01OHf7FR3c
bonnbZmhgetlvet9QZgn8L44L0ISgaL0VEq5BBEOPXW69ScZ89T4U / xKJ8fR
s76qvX / 4
qXBo7uQPCj / WN + 16
pg0nqRAXlmxNlWHDpkSh2bdZwhC9zPvg5jQL
UkJPfrtdjgNczrfLYd3P0AzNZ32ULg2Mz188e540gPK2P36ke5UEgQbZyQFe
oqD / 4
vYHvA8LOnKven7E / I2d5tZtoMoCqU + / Zro1eeAvPljfcgLjpvP / kbYm
DSKziKByii0JCmzznxWdxcNEzakjZeQJZOZlo9ZxAPOUdYO6SuHjSLezMENA
CPO6tT2dtr8FwPjwfrXrPNhc1NqrwiMxrmFT8uwdxMDOJfzpgy9UUNjufDV7
IwVK9w1VuNnhwVAqfJHAEQDFoIMCD9 / zgVeuBPFWAxMgjqhN2 / keOZxW8L7A
pMDE3moDPX0c3Non2675mgqc0JV8 + / ofaMhew1GPScD67pRtghAZrIyERm + s
4
CDy2 / oXraJYD8pYTButCoCKWsbQoRUi2DSuFgUUYVxu1 / nCYJYXvPO3Pjf +
ww / ysa / eX9yI + fImv1eHM7BejqEXhIUwwDzhrBwHcRH9ZPqnvlgCKHYbxgU7
88
Hu42XG5x7TwFLAPH9ohQJWR / XLepwxbti0 + 2
f2VzrkXeP / 6
SnBCx47W6gE
Iewe9qw08BkRwDVw2ioY2FCh5cEZePgN9ZM1LCXtCCBlxNm4r2oB5U2vjyVg
ud7cV / 72
Ac8Sit626xuLLgiJGzUmS06R4HrFU7m6bQzsXGXiMuYa0B09Y3cn
PqyHS + / kaa6dRMJaxS + / KeLBqXndcgrvb5Tx7nf0 / OcZNKHytmwqQRAi / o5l
NXBEgSN5SPjKWzFwjR4ntDryQQrX7JcNiQhB0sdubnjFCz6mdcGFJrwQtMcU
d0oHu6e6gmCyxEUDbvRHKopk0O34RDBMWkHFpIOVXRUU8OZ + JdsHCUGxH709
/ zoDdH2s7Hg1uGiZpp3 / cz8D9J + bFJ3KpkDvw2ZXOSU6NK1RU1h8zALY / Fha
UAPzxTn / fZ1ebOi / G3CA2z + NEu1yMwZCWeCz737If0wugsbnBie + Yz5YkCyb
c + 81U
rwsyfgVRwQnzZCHwqpYHpcPXn9Y + QuRZY3 / he / sQlUErV7pNdPIuL / U
7
FoqtpdmuYSDiXjAHd3n9uAqDbQuJRfjX7BhaofaHgsPBjjZuqUlHhaG + bYb
uHXTePANV75kYUaEjvq6X8L7cED8z + dnV94syqjqEKwOXEDyP / bLUZRYENP2
krwtnw0d5ZdV9AVFocin0UI1ahV1eEhnT7K4qODko + W / t7CeSohj3t / MDzYr
/ DHq + jSQbVqy / 7
t5HJFXH2zNnKLDj8seXG4wEyTsU / PuOk4j9eKICpNKIZhQ
jnpofoAHSnWd95VdEQAwDJyIeUYBak6nwi3Mu0CSzZkz7UZdUttOiIuzAZy6
NH1GBaHogaJz8zcyFB9XVly6w4DVi5vnfY0xXw / OeO9 / EfO3wpxzArnLyIs9
fWJdEXaeSusXHYIYkCLkK0gK / ILy1O + 29
G0YQyPieYOD8nQwjuaGZX75h3z1
P9pXfML6Dffl + es786hD + AD7IsZnJ897X2p / wITPfpMT3FIWNP / 8U
hmWwgtM
4
b41Cbsp0LXgUa6NcX7zxw / 4
g / pTiJMzFXNgZRF53PuwaXcCDbIqe55OD2F8
PlAeKv5qEOlSTIjyV3CwXHdN / sM1UWjmnJ1tHZ5A6h4KsuNZFJhPcAlKeryC
pIqJdPwf7P6El32JPVOPPDrKlReoP5CUzUzz + NkxFKY6HJX3f39T31hi / Xge
+ TynKOdu7EUXv4VuSMzA + CbiSa57LRGKlLOdRh7 + RpzGV80WVxuR / bfA7YvP
8
BAmIqjEFsA47U6Vv6c6C4zr3NM6FmbQTOGyc4IKCayigeMyTgeJ57miJSpL
qDAt3kZflAawVo / 7
rgmbt8rlt0rXqOD6r2yZoECEthqBgdTeJeTk / LbFe7AH
eXxuHrbEfCmw6 / GzxphqVBPPtfN + M488FPXkv0xzUZH5JbPZcD6Y2De4VvGD
CMyT / kRnxIvCyKhNvAl3HqkGVfHoCq + BlKW7UplvviJyZWnW / COsF + 5J
2
FdI
5
iPA627lnce4xkw6xWQ / HRLtB4L6RJhQdkDOiOPKBo3DxdvX6zFBvcac + ukV
C4b0bdYZn2VCxGS0bOjbaRT / VXzMuJYKIJO39YBHM1ouS / L8vJMHrizXUAQw
7
qt4Kr9s7FCOhHV0Mn / M48BDZf6RUOUYUh + 9
f7ek6P / 8 / 5
mEr45Em8xir9S5
zKKOYamnadYiIBEWzTEMnkCyvf6pfne4SPVt / rVkkigQew0CPkcxwfiEzO6R
dyJgGOtereXNC2as3T3vtk + iqnbNqHXHJ5HiH5nZfcW / UZGn + K7tt6eQ8fH +
mNazi8g160vMMSlRyKG7tBZR8BCJW + simC4GPG + t9zgtkMFDp + z8Br9l1MHP
9
pB3xnJ / 5
M2qnswkyrFL6e4spoB09q9Fmi4Lzl6RqRONY8JfyNI2PMiAjudJ
Bt3LJPD90Muf2EABKduo / 8
of0CH6pun6euzn1T3zH5pWUOHsunKFvot0YBNs
rxd7ryBCtlqbt5owFGg7PS0sxD4HTV / V2poAzZ3VN7J3Y3uyM3cPDeNFlT + Z
XiXZc6hD6 / TO0J + Yl6bKJepodqIi9cHEXwli0Oa7RkoHsLw8Zc1gPmxC9Qaz
5
OR5InDc8JHDuUKg2qtHl9YWAdEiTsGABrZPUv6le6 / yQtUdwyT6WUGQe2Ov
c / 4J
Dar7WnQvybGhN3qP7VAY5qVOTVIdP5ZRymanRwHjDDAWl7SOx3gwKKD2
dk8EP0Rrmq1bURQFGw32D1zmOGJr7yU / mltFKbWxzc1Gg2g55feZI34YV3G1
fl6Q70ecJD8BVcynbO7H8Risw / yT6aGtvIiDfrLANo1O7Jwilw5 + 8
REDDUcF
I8VsGiheXzPxq0gYnDLNVFzPY + 8
btf / lgp13x9ydbnkhMUhRqwt2PV2PyEMV
JhtM2VD1a44zUCQIile + Bsl3tiDZ4wOP9nf / RhIXJAgtbzHe9NNyj9FhQsM5
T72ejZjPbJsbeXmDBB4E7izf3BISjJrc5buVAg3SnfK4HDaYeKkJnp5iwcSU
ataL // +f73onr / vVG8j13LapoHysD14fFWu + gOXZ + J / I70GLyPdA7lhTDMbR
Yo + nejJ4QANovi2mTMj7kKgloNqNArfcPpnuX4 / EPz5tGERUeHzERu7wISro
nhjy43uxgnw5yd9kLmP8 + zDkvNftCUS0C0oKNcdyrylVedEaD0GbN7cS9cQg
z7RMVEFlFrEFrt273Ibx35vpOAfNGVRjeTvtexgBDK38LXSuEUCY + eSGhjUV
LgbVHXW / iXnvecmXfBNUwEk8C7lf149KP9 + Kj9s2geTXWnVYJnBRyrGGLyTz
WuS0 / faZWsyvChpYI4GnCFDz9PiaPfVCQJc / xM3 + JAj2HMcP448JcIiru2P +
FBNiTvM09Gth3FHSp1R9Xwy0HxH845V5wUY20sQplw8iS1YHI1wE4Momp / Xe
TVRoe5Sw / Rvm + V1bB0Idj1MghVCk1P54FZUe93jIg / VDbhTHwDcbyxWxzJ + y
Fu3oGY5 / YNaFDlqRffJtXlRokrr / a8f3P6jUV12luhbLkcMXnt9X60fR / gWX
p2qIAHnauCdBJIjUGD0ok4z1q8x096PVRZQTtl5z9vQMMo7IXf1rS4Qwq12r
GfksqL9yPFXQH / OMvs03byYLgqzIx1eRpljupy + 5J
CpOoSK / 9
ZEBvKKgxs5M
vdiIedgHhgzJdxpxSnLsY5 + MIZsIhV9HoprR4l4b2dYUJlSw + W2UDmO8JvZH
ixyHebfrXfHPF0nQ / yU6JQHjHZzB6yONo0 + QRz0xeeYrDaT227XePzeFJgy /
Ri / jsV6 / vGKds7MTqaXreEV6YfliXh58p3wBBWWOG17WmUN2fS9KwiXXgPdL
k873DwRBo819NgCbI8Eo5aeKy // 9
GvlUyI + jnBMqjvaKvLDYLRtwmMiAEHN9
5
cImETD + Q7DT385FEw6jpiZZRIg72gTlCxQIvHvKcuNgCwIpYXsbt2JkNy00
q4TxR5bXqxQxJzKYx1DT0lNw2P2sOr5 / EPMWq68zfooLKDFpoBlZCILKteLQ
vpssaHuQR5i6tIgiF83DpG5jvGLVM2RKwbhKSVG8HvPwSFnjqYi7WI54yAZb
NOFBfnis + fAuIZAqLXn2U2cZVbjftGbveYOy8hfKSdk4MKvQ5f0mTwH / 2
i / 7
9
PcxgJxflmuNX0Cc7U + zCxb + IuGERpVkFg4CU5C8wYkPaKysI4GfQYflSg8J
2
ZsU8KoWqdw0RYO2zpgnA + J8wL6qUq8aO44KLj5nnmTgwepbojtTiwLVrLEd
G / bRYNOw8V1fu0kka1 / h / mADE3Drrz0 + / 5
YAu9sonDR / NsRpSVx9vQPzwtEH
JZ / kRcCqUPIlI1sMIt8HGrzdKQQRqhnpNn / IoLCfI / bSkAFBFjGd66ZnUdtJ
e4muvDmEK5TS8MoZQnFz / 5
V8CB5CQ6ve + Av1K8hK41280mMmDLVFu2as4YWc
+ 1 + VJz7zQobDjqaJ33TwaZTuk5XA + nH77dCJVjx45Dx / tMm2G3F + X6ou7hOG
uC1u69Ppy8gplibhEkWBnKmLH8gH6aD6ox0OmYqAz5NWybqEWXTf6rSslg4Z
Qn79EX1Qv4S + FRb5FdNooP6v75qoyTxaZ3Q4 / XM5BXj69fryuFhelKNam4hJ
ZKZM937 + GdtT5iXnc1cJgIu8cdLS0gZF7ujVK5NeRjZRi22WEWJgLO3I2C9D
AeHNnoq0JFFo2nHtnfhkL6oYu + ukscKG6z81Bb4MsMHJOz / pmBH23HvvVMVm
9
SLViX3Z / Q7C0PbUtcxakgVBZYHTBQ5LKCsrUYRQwg8VZVdrXrAx3t + ZuspN
FYayrlfXXmN7LXdce5NOHR27xzRAC1hfHn0irtcwj / 4
HFWJSbQ ==

"], $CellContext`qf$$ = {5, 5}, $CellContext`qs$$ = {1,
1}, $CellContext
`r$$ = 0.14, $CellContext
`restart$$ =
False, $CellContext
`rold$$ = 0.14, $CellContext
`showConfigObs$$ =
True, Typeset
`show$$ = True, Typeset
`bookmarkList$$ = {},
Typeset
`bookmarkMode$$ = "Menu", Typeset
`animator$$,
Typeset
`animvar$$ = 1, Typeset
`name$$ = "\"untitled\"",
Typeset
`specs$$ = {{{
    Hold[$CellContext
`qf$$], {5, 5}}, {-0.1, -0.1}, {
    6.5973445725385655
`, 6.5973445725385655
`}}, {{
    Hold[$CellContext
`qs$$], {1, 1}}, {-0.1, -0.1}, {
    6.5973445725385655
`, 6.5973445725385655
`}}, {{
    Hold[$CellContext
`pts$$], {}}, 0}, {{
    Hold[$CellContext
`addPoints$$], False}, 0}, {{
    Hold[$CellContext
`restart$$], True}, 0}, {
    Hold[
        Button[
            "add 50 vertices", $CellContext
`addPoints$$ = True, ImageSize ->
140]], Manipulate
`Dump`
ThisIsNotAControl}, {{
    Hold[$CellContext
`r$$], 0.5, "radius"}, 0, 1, 0.01}, {
    Hold[$CellContext
`progress$$], 0, 1, 0.01}, {{
    Hold[$CellContext
`showConfigObs$$], False, "show obstacles"}, {
    False, True}}, {
    Hold[
        Button[
            "restart", $CellContext
`restart$$ = True, ImageSize -> 140]],
Manipulate
`Dump`
ThisIsNotAControl}, {{
    Hold[$CellContext
`path$$], -1}, 0}, {{
    Hold[$CellContext
`rold$$], -1}, 0}, {{
    Hold[$CellContext
`badPts$$], {}}, 0}, {{
    Hold[$CellContext
`goodPts$$], {}}, 0}, {{
    Hold[$CellContext
`edgesNN$$], {}}, 0}, {{
    Hold[$CellContext
`edgesNNadj$$], {}}, 0}, {{
    Hold[$CellContext
`polyN$$], 4}, 0}, {{
    Hold[$CellContext
`polySides$$], {}}, 0}, {{
    Hold[$CellContext
`polys$$], {}}, 0}, {{
    Hold[$CellContext
`polyXY$$], {}}, 0}}, Typeset
`size$$ = {
    450., {234., 240.}}, Typeset
`update$$ = 0, Typeset
`initDone$$,
Typeset
`skipInitDone$$ = False, $CellContext
`qf$9433$$ = {0,
              0}, $CellContext
`qs$9434$$ = {0, 0}, $CellContext
`r$9435$$ =
0, $CellContext
`progress$9436$$ =
0, $CellContext
`showConfigObs$9437$$ = False},
DynamicBox[Manipulate
`ManipulateBoxes[
 1, StandardForm,
 "Variables": > {$CellContext
`addPoints$$ =
False, $CellContext
`badPts$$ = {}, $CellContext
`edgesNN$$ = \
    {}, $CellContext
`edgesNNadj$$ = {}, $CellContext
`goodPts$$ = {}, \
    $CellContext
`path$$ = -1, $CellContext
`polyN$$ =
4, $CellContext
`polys$$ = {}, $CellContext
`polySides$$ = {}, \
    $CellContext
`polyXY$$ = {}, $CellContext
`progress$$ =
0, $CellContext
`pts$$ = {}, $CellContext
`qf$$ = {5,
         5}, $CellContext
`qs$$ = {1, 1}, $CellContext
`r$$ =
0.5, $CellContext
`restart$$ =
True, $CellContext
`rold$$ = -1, $CellContext
`showConfigObs$$ =
False}, "ControllerVariables": > {
    Hold[$CellContext
`qf$$, $CellContext
`qf$9433$$, {0, 0}],
Hold[$CellContext
`qs$$, $CellContext
`qs$9434$$, {0, 0}],
Hold[$CellContext
`r$$, $CellContext
`r$9435$$, 0],
Hold[$CellContext
`progress$$, $CellContext
`progress$9436$$,
0],
Hold[$CellContext
`showConfigObs$$, \
    $CellContext
`showConfigObs$9437$$, False]},
"OtherVariables": > {
    Typeset
`show$$, Typeset
`bookmarkList$$, Typeset
`bookmarkMode$$,
Typeset
`animator$$, Typeset
`animvar$$, Typeset
`name$$,
Typeset
`specs$$, Typeset
`size$$, Typeset
`update$$,
Typeset
`initDone$$, Typeset
`skipInitDone$$}, "Body": >
Module[{$CellContext
`qsni$, $CellContext
`qfni$, \
    $CellContext
`qsn$ = {}, $CellContext
`qfn$ = {}, $CellContext
`delta$ =
0.1, $CellContext
`totdist$},
If[$CellContext
`restart$$, $CellContext
`restart$$ =
False; $CellContext
`polyN$$ = 4; $CellContext
`polySides$$ =
RandomInteger[{3,
               7}, $CellContext
`polyN$$]; $CellContext
`polys$$ =
Map[CirclePoints, $CellContext
`polySides$$]; \
    $CellContext
`polyXY$$ =
RandomReal[{
    0, 2 Pi}, {$CellContext
`polyN$$,
2}]; $CellContext
`polys$$ = Table[
    Map[Part[$CellContext
`polyXY$$, $CellContext
`i] +  # & , 

Part[$CellContext
`polys$$, $CellContext
`i]], \
    {$CellContext
`i,
1, $CellContext
`polyN$$}]; $CellContext
`badPts$$ = {}; \
    $CellContext
`goodPts$$ = {}; $CellContext
`pts$$ = {}; \
    $CellContext
`edgesNN$$ = {}; $CellContext
`edgesNNadj$$ = {};
Null];
If[Part[$CellContext
`qs$$, 1] < 0, Part[$CellContext
`qs$$, 1] =
2
Pi]; If[
    Part[$CellContext
`qs$$, 1] > 2
Pi,
Part[$CellContext
`qs$$, 1] = 0];
If[Part[$CellContext
`qs$$, 2] < 0, Part[$CellContext
`qs$$, 2] =
2
Pi]; If[
    Part[$CellContext
`qs$$, 2] > 2
Pi,
Part[$CellContext
`qs$$, 2] = 0];
If[Part[$CellContext
`qf$$, 1] < 0, Part[$CellContext
`qf$$, 1] =
2
Pi]; If[
    Part[$CellContext
`qf$$, 1] > 2
Pi,
Part[$CellContext
`qf$$, 1] = 0];
If[Part[$CellContext
`qf$$, 2] < 0, Part[$CellContext
`qf$$, 2] =
2
Pi]; If[
    Part[$CellContext
`qf$$, 2] > 2
Pi,
Part[$CellContext
`qf$$, 2] = 0];
If[$CellContext
`addPoints$$, $CellContext
`addPoints$$ = False;
Module[{$CellContext
`newpts$, $CellContext
`point2start$}, \
    $CellContext
`point2start$ =
Length[$CellContext
`goodPts$$] + 1; $CellContext
`newpts$ =
RandomReal[{0, 2 Pi}, {50, 2}]; $CellContext
`pts$$ =
Join[$CellContext
`pts$$, $CellContext
`newpts$]; Table[
    If[
$CellContext
`ptInPolys[$CellContext
`polys$$,
Part[$CellContext
`newpts$, $CellContext
`i]],
AppendTo[$CellContext
`badPts$$,
Part[$CellContext
`newpts$, $CellContext
`i]],
AppendTo[$CellContext
`goodPts$$,

Part[$CellContext
`newpts$, $CellContext
`i]]], \
    {$CellContext
`i, 1,
Length[$CellContext
`newpts$]}];
If[Length[$CellContext
`goodPts$$] > \
    $CellContext
`point2start$ - 1, $CellContext
`edgesNNadj$$ =
Join[$CellContext
`edgesNNadj$$,

ConstantArray[{},
Length[$CellContext
`goodPts$$] - \
    $CellContext
`point2start$ + 1]];
If[$CellContext
`r$$ >
0, {$CellContext
`edgesNNadj$$, \
    $CellContext
`edgesNN$$} = \
    $CellContext
`connectPoints[$CellContext
`goodPts$$, \
    $CellContext
`edgesNNadj$$, $CellContext
`polys$$, $CellContext
`delta$, \
    $CellContext
`edgesNN$$, $CellContext
`point2start$, \
    $CellContext
`r$$]]]; Null]]; If[

    And[$CellContext
`r$$ != $CellContext
`rold$$,
Length[$CellContext
`goodPts$$] >
5], $CellContext
`rold$$ = $CellContext
`r$$; \
    $CellContext
`edgesNN$$ = {}; $CellContext
`edgesNNadj$$ =
ConstantArray[{},
Length[$CellContext
`goodPts$$]];
If[$CellContext
`r$$ >
0, {$CellContext
`edgesNNadj$$, $CellContext
`edgesNN$$} = \
    $CellContext
`connectPoints[$CellContext
`goodPts$$, \
    $CellContext
`edgesNNadj$$, $CellContext
`polys$$, $CellContext
`delta$, \
    $CellContext
`edgesNN$$, 1, $CellContext
`r$$];
Null]]; $CellContext
`path$$ = -1;
If[

    And[$CellContext
`toroidDist[$CellContext
`qs$$, \
    $CellContext
`qf$$] < $CellContext
`r$$,
$CellContext
`pathOKT[$CellContext
`qs$$, $CellContext
`qf$$, \
    $CellContext
`polys$$, $CellContext
`delta$]], $CellContext
`path$$ = -2,
If[
    And[
        Not[
$CellContext
`ptInPolys[$CellContext
`polys$$, \
    $CellContext
`qs$$]], Length[$CellContext
`goodPts$$] > 5],
Do[
    If[
$CellContext
`pathOKT[$CellContext
`qs$$, \
    $CellContext
`pe, $CellContext
`polys$$, $CellContext
`delta$], \
    $CellContext
`qsn$ = $CellContext
`pe;
Break[]], {$CellContext
`pe,
Quiet[

    Nearest[$CellContext
`goodPts$$, $CellContext
`qs$$, 1,
DistanceFunction -> $CellContext
`toroidDist]]}]]; If[
    And[
        Not[
$CellContext
`ptInPolys[$CellContext
`polys$$, \
    $CellContext
`qf$$]], Length[$CellContext
`goodPts$$] > 5],
Do[
    If[
$CellContext
`pathOKT[$CellContext
`qf$$, \
    $CellContext
`pe, $CellContext
`polys$$, $CellContext
`delta$], \
    $CellContext
`qfn$ = $CellContext
`pe;
Break[]], {$CellContext
`pe,
Quiet[

    Nearest[$CellContext
`goodPts$$, $CellContext
`qf$$, 1,
DistanceFunction -> $CellContext
`toroidDist]]}]];
Null]; If[

    And[$CellContext
`qfn$ != {}, $CellContext
`qsn$ != {},
Length[$CellContext
`edgesNNadj$$] > 1], $CellContext
`qsni$ =
Part[

    Position[$CellContext
`goodPts$$, $CellContext
`qsn$, 1,
1], 1, 1]; $CellContext
`qfni$ = Part[

    Position[$CellContext
`goodPts$$, $CellContext
`qfn$, 1,
1], 1, 1]; $CellContext
`path$$ = \
    $CellContext
`myAstar[$CellContext
`edgesNNadj$$, \
    $CellContext
`goodPts$$, $CellContext
`qsni$, $CellContext
`qfni$];
Null]; Graphics[{
    If[$CellContext
`showConfigObs$$, {Pink,
                   Polygon[$CellContext
`polys$$]}],
$CellContext
`toroidLines[$CellContext
`edgesNN$$, LightBlue,
Blue],
If[
    And[
        Length[$CellContext
`path$$] ==
0, $CellContext
`path$$ == -2], {
    Thickness[0.02],
$CellContext
`toroidLine[{$CellContext
`qs$$, \
    $CellContext
`qf$$},
Magenta], $CellContext
`totdist$ = \
    $CellContext
`toroidDist[$CellContext
`qs$$, $CellContext
`qf$$]; Purple,
PointSize[0.04],
Point[
$CellContext
`toroidPt[{$CellContext
`qs$$, \
    $CellContext
`qf$$}, $CellContext
`progress$$]]},
If[Length[$CellContext
`path$$] > 0, {
    Thickness[0.02],
$CellContext
`toroidLine[{$CellContext
`qs$$, \
    $CellContext
`qsn$}, Magenta],
$CellContext
`toroidLine[{$CellContext
`qf$$, \
    $CellContext
`qfn$}, Magenta],
Table[
$CellContext
`toroidLine[{
    Part[$CellContext
`goodPts$$,
Part[$CellContext
`path$$, $CellContext
`i]],
Part[$CellContext
`goodPts$$,
Part[$CellContext
`path$$, $CellContext
`i + 1]]},
Lighter[Green], Green], {$CellContext
`i, 1,
Length[$CellContext
`path$$] - 1}], Black,
Point[$CellContext
`qs$$],
Point[$CellContext
`qf$$],

Module[{$CellContext
`dists$, $CellContext
`c$, \
    $CellContext
`distT$, $CellContext
`mypath$ = Append[
    Prepend[

        Part[$CellContext
`goodPts$$, $CellContext
`path$$], \
    $CellContext
`qs$$], $CellContext
`qf$$]}, $CellContext
`dists$ = Table[
$CellContext
`toroidDist[
    Part[$CellContext
`mypath$, $CellContext
`i],

Part[$CellContext
`mypath$, $CellContext
`i +
 1]], {$CellContext
`i, 1,
Length[$CellContext
`mypath$] -
1}]; $CellContext
`totdist$ =
Total[$CellContext
`dists$]; $CellContext
`distT$ =
0; $CellContext
`c$ = 1;
While[$CellContext
`distT$ +
Part[$CellContext
`dists$, $CellContext
`c$] < \
    $CellContext
`progress$$ $CellContext
`totdist$,
AddTo[$CellContext
`distT$,
Part[$CellContext
`dists$, $CellContext
`c$]];
Increment[$CellContext
`c$]]; {Purple,
        PointSize[0.04],
        Point[
$CellContext
`toroidPt[{
    Part[$CellContext
`mypath$, $CellContext
`c$],
Part[$CellContext
`mypath$, $CellContext
`c$ +
1]}, ($CellContext`progress$$ \
          $CellContext`totdist$ - $CellContext`distT$) /
     Part[$CellContext
`dists$, $CellContext
`c$]]]}]}, {
    If[$CellContext
`qsn$ != {},
$CellContext
`toroidLine[{$CellContext
`qs$$, \
    $CellContext
`qsn$}, Magenta]],
If[$CellContext
`qfn$ != {},
$CellContext
`toroidLine[{$CellContext
`qf$$, \
    $CellContext
`qfn$}, Magenta]]}]],
Darker[Green],
PointSize[Medium],
Point[$CellContext
`goodPts$$], Red,
Point[$CellContext
`badPts$$],
Locator[$CellContext
`qs$$,
If[
$CellContext
`ptInPolys[$CellContext
`polys$$, \
    $CellContext
`qs$$],
$CellContext
`loc[Red],
$CellContext
`loc[
    Darker[Green]]]],
Locator[$CellContext
`qf$$,
If[
$CellContext
`ptInPolys[$CellContext
`polys$$, \
    $CellContext
`qf$$],
$CellContext
`loc[Red],
$CellContext
`loc[
    Darker[Green]]]]}, PlotLabel -> If[
    And[
        Length[$CellContext
`path$$] ==
0, $CellContext
`path$$ == -1], "no path possible",
StringForm["path length = ``",
Round[$CellContext
`totdist$, 0.01]]], Axes -> True,
AxesOrigin -> {0, 0}, PlotRange -> {{0, 2 Pi}, {0, 2 Pi}}]],
"Specifications": > {{{$CellContext
`qf$$, {5,
        5}}, {-0.1, -0.1}, {6.5973445725385655
`,
6.5973445725385655
`}, ControlType -> Locator, Appearance ->
None}, {{$CellContext
`qs$$, {1, 1}}, {-0.1, -0.1}, {
    6.5973445725385655
`, 6.5973445725385655
`}, ControlType ->
Locator, Appearance -> None}, {{$CellContext
`pts$$, {}}, 0,
ControlType -> None}, {{$CellContext
`addPoints$$, False}, 0,
ControlType -> None}, {{$CellContext
`restart$$, True}, 0,
ControlType -> None},
Button[
    "add 50 vertices", $CellContext
`addPoints$$ = True, ImageSize ->
140], {{$CellContext
`r$$, 0.5, "radius"}, 0, 1, 0.01,
Appearance -> "Labeled", ImageSize ->
100}, {$CellContext
`progress$$, 0, 1, 0.01, Enabled ->
Dynamic[
    Or[
        Length[$CellContext
`path$$] >
0, $CellContext
`path$$ == -2]], Appearance -> "Labeled",
ImageSize ->
100}, {{$CellContext
`showConfigObs$$, False,
"show obstacles"}, {False, True}},
Button[
    "restart", $CellContext
`restart$$ = True, ImageSize ->
140], {{$CellContext
`path$$, -1}, 0, ControlType ->
None}, {{$CellContext
`rold$$, -1}, 0, ControlType ->
None}, {{$CellContext
`badPts$$, {}}, 0, ControlType ->
None}, {{$CellContext
`goodPts$$, {}}, 0, ControlType ->
None}, {{$CellContext
`edgesNN$$, {}}, 0, ControlType ->
None}, {{$CellContext
`edgesNNadj$$, {}}, 0, ControlType ->
None}, {{$CellContext
`polyN$$, 4}, 0, ControlType ->
None}, {{$CellContext
`polySides$$, {}}, 0, ControlType ->
None}, {{$CellContext
`polys$$, {}}, 0, ControlType ->
None}, {{$CellContext
`polyXY$$, {}}, 0, ControlType ->
None}}, "Options": > {ControlPlacement -> Left},
"DefaultOptions": > {ControllerLinking -> True}],
ImageSizeCache->{724., {267., 273.}},
SingleEvaluation->True],
Deinitialization: > None,
DynamicModuleValues: > {},
Initialization: > ({$CellContext`ptInPolys[
Pattern[$CellContext`polys,
Blank[]],
Pattern[$CellContext`pt,
Blank[]]] := Apply[Or,

Map[$CellContext`ptInPoly[  # , $CellContext`pt]& , \
$CellContext`polys]], $CellContext`ptInPoly[
Pattern[$CellContext`poly,
Blank[]],
Pattern[$CellContext`pt,
Blank[]]] := (Apply[Equal,  # ]& )[
(Map[Apply[$CellContext`angtest,  # ]& , #]& )[
Transpose[
({  # , 
RotateLeft[  # ]}& )[
(
Map[  # - $CellContext`pt& , #]& )[$CellContext`poly]]]]], \
$CellContext`angtest[
Pattern[$CellContext`p1, {
Pattern[$CellContext`x1,
Blank[]],
Pattern[$CellContext`y1,
Blank[]]}],
Pattern[$CellContext`p2, {
Pattern[$CellContext`x2,
Blank[]],
Pattern[$CellContext`y2,
Blank[]]}]] :=
Dot[$CellContext`p1, {{0, -1}, {1, 0}}, $CellContext`p2] >
0, $CellContext`connectPoints[
Pattern[$CellContext`goodPts,
Blank[]],
Pattern[$CellContext`edgesNNadjin,
Blank[]],
Pattern[$CellContext`polys,
Blank[]],
Pattern[$CellContext`delta,
Blank[]],
Pattern[$CellContext`edgesNNin,
Blank[]],
Pattern[$CellContext`point2start,
Blank[]],
Pattern[$CellContext`r,
Blank[]]] :=
Module[{$CellContext`ps, $CellContext`pe, $CellContext`pei, \
    $CellContext`edgesNNadj, $CellContext`edgesNN}, \
    $CellContext`edgesNNadj = $CellContext`edgesNNadjin; \
    $CellContext`edgesNN = $CellContext`edgesNNin;
Table[$CellContext`ps =
Part[$CellContext`goodPts, $CellContext`i];
Table[$CellContext`pei = Part[
Position[$CellContext`goodPts, $CellContext`pe, 1, 1],
1, 1]; If[Count[

Part[$CellContext`edgesNNadj, $CellContext`i], \
    $CellContext`pei] < 1,
If[
$CellContext`pathOKT[$CellContext`ps, \
    $CellContext`pe, $CellContext`polys, $CellContext`delta],
AppendTo[$CellContext`edgesNN, {$CellContext`ps, \
    $CellContext`pe}]; AppendTo[

Part[$CellContext`edgesNNadj, $CellContext`i], \
    $CellContext`pei]; AppendTo[

Part[$CellContext`edgesNNadj, $CellContext`pei], \
    $CellContext`i]; Null]], {$CellContext`pe,
Quiet[
Nearest[

Drop[$CellContext`goodPts, {$CellContext`i}], \
    $CellContext`ps, {10, $CellContext`r},
DistanceFunction -> $CellContext`toroidDist]]}], \
    {$CellContext`i, $CellContext`point2start,

Length[$CellContext`goodPts]}]; {$CellContext`edgesNNadj, \
    $CellContext`edgesNN}], $CellContext`pathOKT[
Pattern[$CellContext`ps,
Blank[]],
Pattern[$CellContext`pe,
Blank[]],
Pattern[$CellContext`polys,
Blank[]],
Pattern[$CellContext`delta,
Blank[]]] :=
Module[{$CellContext`dist, $CellContext`n, $CellContext`pt, \
    $CellContext`dx, $CellContext`dx2, $CellContext`dy, \
    $CellContext`dy2}, $CellContext`dx =
Abs[Part[$CellContext`pe, 1] -
Part[$CellContext`ps, 1]]; $CellContext`dx2 =
2 Pi - $CellContext`dx; $CellContext`dy =
Abs[Part[$CellContext`pe, 2] -
Part[$CellContext`ps, 2]]; $CellContext`dy2 =
2 Pi - $CellContext`dy; $CellContext`dx =
Part[$CellContext`pe, 1] - Part[$CellContext`ps, 1] +
If[$CellContext`dx < $CellContext`dx2, 0,
If[
Part[$CellContext`pe, 1] >
Part[$CellContext`ps, 1], (-2)
Pi, Plus[2]
Pi]]; $CellContext
`dy =
Part[$CellContext
`pe, 2] - Part[$CellContext
`ps, 2] +
If[$CellContext
`dy < $CellContext
`dy2, 0,
If[
    Part[$CellContext
`pe, 2] >
Part[$CellContext
`ps, 2], (-2)
Pi, Plus[2]
Pi]]; $CellContext
`dist =
Sqrt[$CellContext
`dx ^ 2 + $CellContext
`dy ^ 2];
If[$CellContext
`dist <= $CellContext
`delta,
True, $CellContext
`n =
Ceiling[$CellContext
`dist /$CellContext
`delta]; Not[
    Apply[Or,

    Table[$CellContext
`pt = $CellContext
`ps + \
 {$CellContext
`dx, $CellContext
`dy} ($CellContext`i / ($CellContext`n +
      1)); If[
    Part[$CellContext
`pt, 1] < 0,
Part[$CellContext
`pt, 1] =
Part[$CellContext
`pt, 1] + 2
Pi];
If[Part[$CellContext
`pt, 1] > 2
Pi,
Part[$CellContext
`pt, 1] =
Part[$CellContext
`pt, 1] - 2
Pi];
If[Part[$CellContext
`pt, 2] < 0,
Part[$CellContext
`pt, 2] =
Part[$CellContext
`pt, 2] + 2
Pi];
If[Part[$CellContext
`pt, 2] > 2
Pi,
Part[$CellContext
`pt, 2] =
Part[$CellContext
`pt, 2] - 2

Pi]; $CellContext
`ptInPolys[$CellContext
`polys, \
    $CellContext
`pt], {$CellContext
`i,
1, $CellContext
`n}]]]]], $CellContext
`toroidDist :=
Sqrt[Min[(Part[  # , 1] - Part[#2, 1])^2, (2 Pi - Abs[
    Part[  # , 1] - Part[#2, 1]])^2] + 
        Min[(Part[  # , 2] - Part[#2, 2])^2, (2 Pi - Abs[
            Part[  # , 2] - Part[#2, 2]])^2]]& , $CellContext`myAstar[
                Pattern[$CellContext`adjL,
                        Blank[]],
                        Pattern[$CellContext`verts,
                        Blank[]],
                        Pattern[$CellContext`si,
                        Blank[]],
                        Pattern[$CellContext`fi,
                        Blank[]]] :=
                        Module[{$CellContext`openSet, $CellContext`cameFrom, \
                            $CellContext`gScore, $CellContext`fScore, $CellContext`current, \
                            $CellContext`currentfscore, $CellContext`path, \
                            $CellContext`tentativegScore}, $CellContext`openSet = \
                            {$CellContext`si}; $CellContext`cameFrom = ConstantArray[-1,
                        Length[$CellContext`verts]]; $CellContext`gScore =
                        ConstantArray[Infinity,
                        Length[$CellContext`verts]];
                        Part[$CellContext`gScore, $CellContext`si] =
                        0; $CellContext`fScore = ConstantArray[Infinity,
                        Length[$CellContext`verts]];
                        Part[$CellContext`fScore, $CellContext`si] = \
                            $CellContext`toroidDist[
                        Part[$CellContext`verts, $CellContext`si],
                        Part[$CellContext`verts, $CellContext`fi]];
                        While[Length[$CellContext`openSet] >
                        0, $CellContext`currentfscore = Min[

                        Part[$CellContext`fScore, $CellContext`openSet]]; \
                            $CellContext`current = Part[$CellContext`openSet,
                        Apply[First,
                        Position[

                        Part[$CellContext`fScore, $CellContext`openSet], \
                            $CellContext`currentfscore]]];
                        If[$CellContext`current == $CellContext`fi, \
                            $CellContext`path = {$CellContext`fi};
                        While[First[$CellContext`path] != $CellContext`si,
                        PrependTo[$CellContext`path,
                        Part[$CellContext`cameFrom,
                        First[$CellContext`path]]]];
                        Return[$CellContext`path]]; $CellContext`openSet =
                        DeleteCases[$CellContext`openSet, $CellContext`current];
                        Table[$CellContext`tentativegScore =
                        Part[$CellContext`gScore, $CellContext`current] + \
                            $CellContext`toroidDist[
                        Part[$CellContext`verts, $CellContext`current],
                        Part[$CellContext`verts, $CellContext`nbr]];
                        If[$CellContext`tentativegScore <
                        Part[$CellContext`gScore, $CellContext`nbr],
                        Part[$CellContext`cameFrom, $CellContext`nbr] = \
                            $CellContext`current;
                        Part[$CellContext`gScore, $CellContext`nbr] = \
                            $CellContext`tentativegScore;
                        Part[$CellContext`fScore, $CellContext`nbr] =
                        Part[$CellContext`gScore, $CellContext`nbr] + \
                            $CellContext`toroidDist[
                        Part[$CellContext`verts, $CellContext`nbr],
                        Part[$CellContext`verts, $CellContext`nbr]]; If[
                        FreeQ[$CellContext`openSet, $CellContext`nbr],
                        AppendTo[$CellContext`openSet, $CellContext`nbr]]];
                        Null, {$CellContext`nbr,
                        Part[$CellContext`adjL, $CellContext`current]}]; Null];
                        Return[-1]], $CellContext`toroidLines[
                        Pattern[$CellContext`pts,
                        Blank[]],
                        Optional[
                        Pattern[$CellContext`color1,
                        Blank[]],
                        RGBColor[0, 0, 1]],
                        Optional[
                        Pattern[$CellContext`color2,
                        Blank[]], -1]] := Table[
                        $CellContext`toroidLine[$CellContext`e, $CellContext`color1, \
                            $CellContext`color2], {$CellContext`e, $CellContext`pts}], \
                            $CellContext`toroidLine[
                        Pattern[$CellContext`e,
                        Blank[]],
                        Optional[
                        Pattern[$CellContext`color1,
                        Blank[]],
                        RGBColor[0, 0, 1]],
                        Optional[
                        Pattern[$CellContext`color2,
                        Blank[]], -1]] :=
                        Module[{$CellContext`dx, $CellContext`dx2, $CellContext`dy, \
                            $CellContext`dy2}, $CellContext`dx =
                        Abs[Part[$CellContext`e, 2, 1] -
                        Part[$CellContext`e, 1, 1]]; $CellContext`dx2 =
                        2 Pi - $CellContext`dx; $CellContext`dy =
                        Abs[Part[$CellContext`e, 2, 2] -
                        Part[$CellContext`e, 1, 2]]; $CellContext`dy2 =
                        2 Pi - $CellContext`dy; If[

                        Or[$CellContext`dx > $CellContext`dx2, $CellContext`dy > \
                            $CellContext`dy2], $CellContext`dx =
                        Part[$CellContext`e, 2, 1] - Part[$CellContext`e, 1, 1] +
                        If[$CellContext`dx < $CellContext`dx2, 0,
                        If[
                        Part[$CellContext`e, 2, 1] >
                        Part[$CellContext`e, 1, 1], (-2) Pi, Plus[2]
                                                         Pi]]; $CellContext`dy =
                                                         Part[$CellContext`e, 2, 2] - Part[$CellContext`e, 1, 2] +
                                                         If[$CellContext`dy < $CellContext`dy2, 0,
                                                         If[
                                                         Part[$CellContext`e, 2, 2] >
                                                         Part[$CellContext`e, 1, 2], (-2)
Pi, Plus[2]
Pi]]; {$CellContext
`color1,
Line[{
    Part[$CellContext
`e, 1],
Part[$CellContext
`e,
1] + {$CellContext
`dx, $CellContext
`dy}}],
Line[{
    Part[$CellContext
`e, 2],
Part[$CellContext
`e,
2] - {$CellContext
`dx, $CellContext
`dy}}]}, {

    If[-1 == = $CellContext
`color2, $CellContext
`color1, \
    $CellContext
`color2],
Line[$CellContext
`e]}]], $CellContext
`toroidPt[
    Pattern[$CellContext
`e,
Blank[]],
Pattern[$CellContext
`frac,
Blank[]]] :=
Module[{$CellContext
`dx, $CellContext
`dy, $CellContext
`dx2, \
    $CellContext
`dy2, $CellContext
`dist, $CellContext
`pt}, \
    $CellContext
`dx =
Abs[Part[$CellContext
`e, 2, 1] -
Part[$CellContext
`e, 1, 1]]; $CellContext
`dy =
Abs[Part[$CellContext
`e, 2, 2] -
Part[$CellContext
`e, 1, 2]]; $CellContext
`dx2 =
Part[$CellContext
`e, 2, 1] - Part[$CellContext
`e, 1, 1] +
If[$CellContext
`dx < 2
Pi - $CellContext
`dx, 0,
If[
    Part[$CellContext
`e, 2, 1] >
Part[$CellContext
`e, 1, 1], (-2)
Pi, Plus[2]
Pi]]; $CellContext
`dy2 =
Part[$CellContext
`e, 2, 2] - Part[$CellContext
`e, 1, 2] +
If[$CellContext
`dy < 2
Pi - $CellContext
`dy, 0,
If[
    Part[$CellContext
`e, 2, 2] >
Part[$CellContext
`e, 1, 2], (-2)
Pi, Plus[2]
Pi]]; $CellContext
`dist =
Sqrt[$CellContext
`dx2 ^ 2 + $CellContext
`dy2 ^ 2];
If[$CellContext
`dist == 0, $CellContext
`pt =
Part[$CellContext
`e, 1], $CellContext
`pt =
Part[$CellContext
`e,
1] + $CellContext
`frac
{$CellContext
`dx2, \
    $CellContext
`dy2};
Part[$CellContext
`pt, 1] =
Part[$CellContext
`pt, 1] +
If[Part[$CellContext
`pt, 1] > 2
Pi, (-2)
Pi,
If[Part[$CellContext
`pt, 1] < 0, 2
Pi, 0]];
Part[$CellContext
`pt, 2] =
Part[$CellContext
`pt, 2] +
If[Part[$CellContext
`pt, 2] > 2
Pi, (-2)
Pi,
If[Part[$CellContext
`pt, 2] < 0, 2
Pi, 0]];
Null]; $CellContext
`pt], $CellContext
`loc[
    Pattern[$CellContext
`col,
Blank[]]] := ToExpression[
    GraphicsBox[{$CellContext
`col, {
    AbsoluteThickness[1], Antialiasing -> False,

LineBox[{{{0, -10}, {0, -2}}, {{0, 2}, {0, 10}}, {{-10,
                                                   0}, {-2, 0}}, {{2, 0}, {10, 0}}}], Antialiasing -> True,

CircleBox[{-0.5, 0.5}, 5]}, {
    AbsoluteThickness[3],
    Opacity[0.3],
    CircleBox[{-0.5, 0.5}, 3]}}, ImageSize -> 17,
PlotRange -> {{-8, 8}, {-8, 8}}]],
Attributes[PlotRange] = {ReadProtected}};
Typeset
`initDone$$ = True),
SynchronousInitialization->True,
UndoTrackedVariables: > {Typeset
`show$$, Typeset
`bookmarkMode$$},
UnsavedVariables: > {Typeset
`initDone$$},
UntrackedVariables: > {Typeset
`size$$}], "Manipulate",
Deployed->True,
StripOnInput->False],
Manipulate
`InterpretManipulate[1]]], "Output",
CellGroupingRules->{"GroupTogetherGrouping", 5646.},
CellChangeTimes->{3.787451841081852 * ^ 9, 3.788641593869904 * ^ 9},
CellID->169941195]
}, {13}]]

