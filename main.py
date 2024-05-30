from manim import *
import math 
import mpmath

class taylor_series(Scene):
    def construct(self):
        
        
        e_taylor = MathTex(r"e^{x}=1+ x^1 + \frac{1}{2!} x^2 + \frac{1}{3!} x^3 +\frac{1}{4!}x^4 \cdots + \frac{1}{n!} x^n + \cdots", substrings_to_isolate= "x").shift(UP*2)
        e_taylor.set_color_by_tex("x", TEAL_D)
        eq = MathTex("z","=","a", "+", "bi")
        eq2 = MathTex("z","=","\\cos(\\theta)", "+", "\\sin(\\theta)i")
        eq3 = MathTex("z","=","\\cos(\\theta)", "+", "i\\sin(\\theta)")
        eq4 = MathTex("z","=","(1-\\frac{\\theta^{2}}{2!}+\\frac{\\theta^{4}}{4!}-\\frac{\\theta^{6}}{6!}+...)", "+", "i(\\theta-\\frac{\\theta^{3}}{3!}+\\frac{\\theta^{5}}{5!}-\\frac{\\theta^7}{7!}+...)")
        eq5 = MathTex("z","=","(1-\\frac{\\theta^{2}}{2!}+\\frac{\\theta^{4}}{4!}-\\frac{\\theta^{6}}{6!}+...)","+","i\\theta -i\\frac{\\theta^3}{3!} + i\\frac{\\theta^5}{5!}-i\\frac{\\theta^7}{7!}+...")
        eq6 = MathTex("z","=","1 + i\\theta -\\frac{\\theta^{2}}{2!} -i\\frac{\\theta^3}{3!}+\\frac{\\theta^{4}}{4!}+ i\\frac{\\theta^5}{5!}-\\frac{\\theta^{6}}{6!}-i\\frac{\\theta^7}{7!}+...")
        eq7 = MathTex("z","=","1 + i\\theta +i^2\\frac{\\theta^{2}}{2!} +i^3\\frac{\\theta^3}{3!}+i^4\\frac{\\theta^{4}}{4!}+ i^5\\frac{\\theta^5}{5!}+i^6\\frac{\\theta^{6}}{6!}+i^7\\frac{\\theta^7}{7!}+...").scale(0.9)
        eq9 = MathTex(r"z =1+{{i\theta^}}1 + \frac{1}{2!} {{i\theta}}^2 + \frac{1}{3!} {{i\theta}}^3 +\frac{1}{4!}{{i\theta}}^4+ \frac{1}{5!}{{i\theta}}^5+\frac{1}{6!}{{i\theta}}^6+\frac{1}{7!}{{i\theta}}^7+ \cdots").scale(0.9)
        eq9_div = MathTex(r" e^{i\theta} =1+{{i\theta^}}1 + \frac{1}{2!} {{i\theta}}^2 + \frac{1}{3!} {{i\theta}}^3 +\frac{1}{4!}{{i\theta}}^4+ \frac{1}{5!}{{i\theta}}^5+\frac{1}{6!}{{i\theta}}^6+\frac{1}{7!}{{i\theta}}^7+ \cdots").scale(0.9)
        lista=[1,3,5,7,9,11,13]
        for i in lista:
            eq9_div[i].set_color(TEAL_D)
        eq10 = MathTex("e^{i\\theta}" ,"=","\\cos(\\theta)", "+", "i\\sin(\\theta)")
        finale = MathTex("e^{i\\pi}" ,"=","\\cos(\\pi)", "+", "i\\sin(\\pi)")
        finale2 = MathTex("e^{i\\pi}" ,"=","-1", "+", "0")
        finale3 = MathTex("e^{i\\pi}" ,"=","-1")
        self.add(eq)
        self.wait(2)
        self.play(ReplacementTransform(eq,eq2))
        self.wait()
        self.play(ReplacementTransform(eq2,eq3))
        self.wait()
        self.play(ReplacementTransform(eq3,eq4))
        self.wait()
        self.play(ReplacementTransform(eq4,eq5))
        self.wait()
        self.play(ReplacementTransform(eq5,eq6))
        self.wait()
        self.play(ReplacementTransform(eq6,eq7))
        self.wait()
        self.play(ReplacementTransform(eq7,eq9),Write(e_taylor))
        self.wait()
        self.play(ReplacementTransform(eq9,eq9_div))
        self.wait()
        self.play(ReplacementTransform(eq9_div,eq10), Unwrite(e_taylor))
        self.wait()
        self.play(ReplacementTransform(eq10,finale))
        self.wait()
        self.play(ReplacementTransform(finale, finale2))
        self.wait()
        self.play(ReplacementTransform(finale2, finale3))
        self.wait(
            2
        )

class e(Scene):
    def construct(self):

        titolo = MathTex("1.","e").scale(3)
        self.play(Write(titolo))
        self.wait()
        
        e = MathTex("e").scale(2)
        xponential = MathTex("xponential").scale(0.6).shift(DOWN*0.1).shift(RIGHT*0.9)
        self.play(TransformMatchingTex(titolo,e))
        
        growth = MathTex("e","= \\lim_{n\\to \\infty }\\left(  1 + \\frac{1}{n}\\right)^n").shift(RIGHT*2)
        compound_interest = Tex("Compound interest").scale(1.3).next_to(growth, UP, buff = 0.2)
        euler = ImageMobject("eulero").to_edge(LEFT,buff= 0).shift(LEFT*4.6)
        bernoulli = ImageMobject("bernoulli").scale(1.5).to_edge(LEFT,buff = 0).shift(DOWN*8)

        k= ValueTracker(-2)

        
        derivata_e = MathTex("\\frac{d}{dx}e^x = e^x", substrings_to_isolate= "x").scale(2).shift(LEFT*3)
        derivata_e.set_color_by_tex("x", TEAL_D)
        assi = Axes(x_range = [-2,3,1], y_range = [-2,10,2], x_length = 6, y_length= 6, axis_config={"numbers_to_exclude": [-0.5,0.5,1.5,2.5,3.5]}).set_opacity(0.8).add_coordinates(font_size= 24).shift(RIGHT*3, UP*0.5)
        graph = assi.plot(lambda x : np.exp(x), color = TEAL_D, x_range = [-2,2.21])
        graph_label = MathTex("e^x", substrings_to_isolate="x").scale(2).shift(LEFT * 3)
        graph_label.set_color_by_tex("x",TEAL_D)
                              
        dot = always_redraw(lambda: Dot().set_color_by_gradient(TEAL_D, MAROON_B).scale(0.7).move_to(assi.c2p(k.get_value(),graph.underlying_function(k.get_value()))))
      
        text = MathTex(r"e^x = 1+ x^1 + \frac{1}{2!} x^2 + \frac{1}{3!} x^3 +\frac{1}{4!}x^4 \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x")
        text.set_color_by_tex("x", TEAL_E)
    
        text2 = MathTex(r"e^1=1+1+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+ \cdots+\frac{1}{n!}+\cdots").shift(DOWN *2)
        text2_updated = MathTex("e=\\sum^{\\infty }_{n=0}\\frac{1}{n!}=2+\\frac{1}{2!}+\\frac{1}{3!}+\\frac{1}{4!}...").shift(DOWN *2)
        
        moving_slope = always_redraw(lambda : assi.get_secant_slope_group(x = k.get_value(), graph = graph, secant_line_color = MAROON_B, dx = 0.0001, secant_line_length= 3))
        slope1 = Tex("Slope" "= ").next_to(assi,DOWN,buff = 0.2).shift(LEFT*2)
        slope1[0].set_color(MAROON_B)
        slope2 = always_redraw(lambda: DecimalNumber().next_to(slope1,RIGHT,buff= 0.2).set_value(k.get_value()))

        x_line= always_redraw(lambda : Line(start = assi.c2p(0,0), end= assi.c2p(k.get_value(),0), color = YELLOW))
        x_label = MathTex("x", "= ").next_to(slope2, RIGHT, buff = 0.5)
        little_line = always_redraw(lambda: Line( start = assi.c2p(k.get_value(),-0.2), end = assi.c2p(k.get_value(),0.2), color = YELLOW))
        x_label[0].set_color(YELLOW)
        x_number = always_redraw(lambda: DecimalNumber().set_value(k.get_value()).next_to(x_label,RIGHT,buff= 0.2))
        
        self.wait(2)
        self.play(FadeIn(euler)) 
        self.play( euler.animate.shift(RIGHT*4.6))
        self.wait()
        self.play(Write(xponential))
        self.wait()
        self.play(euler.animate.shift(LEFT*4.6), FadeIn(bernoulli), Unwrite(xponential))
        self.play(bernoulli.animate.shift(UP*8), run_time = 2)
        self.play(TransformMatchingTex(e, growth), Write(compound_interest))
        self.wait()
        self.play(Unwrite(compound_interest),ReplacementTransform(growth,e), bernoulli.animate.shift(UP*8), run_time =2)
        self.wait()
        self.play(e.animate.shift(LEFT * 2.5))
        self.play(Write(assi))
        self.play(Create(graph),ReplacementTransform(e, graph_label))
        self.wait()
        self.play(ReplacementTransform(graph_label,derivata_e),Create(moving_slope), Create(dot), Write(slope1), Write(slope2), Write(x_label), Write(x_number), Create(x_line), Create(little_line))
        self.play(k.animate.set_value(2.21), run_time = 4)
        self.wait(2)
        self.play(Unwrite(derivata_e), Unwrite(assi),Uncreate(moving_slope), Uncreate(dot),FadeOut(graph), Unwrite(slope1), Unwrite(slope2), Unwrite(x_label), Unwrite(x_number), Uncreate(little_line),Uncreate(x_line))
        self.play(Write(text), run_time = 3)
        self.wait(2)
        self.play(text.animate.shift(UP*2))
        self.play(Write(text2), run_time = 3)
        self.wait()
        self.play(ReplacementTransform(text2, text2_updated))
        self.wait(4)
        self.play(Unwrite(text2_updated), Unwrite(text))
        self.wait()
      
class pi(Scene):
    def construct(self):
        
        inizio = MathTex(r"2. \pi").scale(3)
        self.play(Write(inizio))
        self.wait()
        self.play(Unwrite(inizio))
        
        circle = Circle(radius = 2,stroke_color = TEAL_D).shift(LEFT * 3)
        dot = Dot(color = RED_C).move_to(circle.get_right()).set_opacity(0)
        radius1 = Line(color = MAROON_C).add_updater(lambda x : x.put_start_and_end_on(start = circle.get_center(),end = dot.get_center()))
        circumference = Line(color = TEAL_D).rotate(90 * DEGREES).next_to(circle,RIGHT, buff = 0.5).set_length(2*PI)
        
        all = VGroup(circle,radius1)
        
        radius_label= MathTex("r" ,"= ", substrings_to_isolate = ["r"]).shift(RIGHT*3, UP *2)
        radius_label.set_color_by_tex("r",MAROON_C)
        radius_value = DecimalNumber(num_decimal_places=2).next_to(radius_label,RIGHT,buff = 0.5).add_updater(lambda x :x.set_value(circle.get_width()/2))

        diameter_label = MathTex("d","=" ,"2","r"," = ", substrings_to_isolate = ["d","r"]).next_to(radius_label, DOWN, buff = 0.5).set_color_by_tex("d",GREEN_E).set_color_by_tex("r",MAROON_C)
        diameter_value = DecimalNumber(num_decimal_places=2).next_to(diameter_label,RIGHT,buff = 0.5).add_updater(lambda x:x.set_value(circle.get_width()))
        
        circumference_label = MathTex("C" ,"=", substrings_to_isolate = ["C"]).next_to(diameter_label, DOWN, buff = 0.5).set_color_by_tex("C", TEAL_D)
        circumference_value = DecimalNumber(num_decimal_places=2).next_to(circumference_label,RIGHT,buff=0.5).add_updater(lambda x:x.set_value(circle.get_width()*PI))

        
        
        self.play(Create(circle), Write(radius_label), Write(radius_value), Write(circumference_label), 
                  Write(circumference_value), Write(diameter_label), Write(diameter_value))
        self.play(Create(radius1),Create(dot))
        self.play(MoveAlongPath(dot,circle, run_time = 2, rate_func = smooth))

        dot.add_updater(lambda x : x.move_to(circle.get_right()))

        self.play(all.animate.scale(0.5))
        radius1.clear_updaters()
        radius2 = Line(start = circle.get_center(), end = circle.get_left(), color = BLUE)
        diameter1 = VGroup(radius1,radius2).set_color(GREEN_E)
        diameter2 = diameter1.copy().set_color(GREEN_C).rotate(PI/2).next_to(diameter1,LEFT,buff = 0.2)
        diameter3 = diameter1.copy().set_color(GREEN_B).rotate(PI/2).next_to(diameter2,LEFT,buff = 1.2)
        
        
        
        self.play(Create(radius2),FadeOut(dot))
        self.play(Rotate(diameter1, angle = 90 * DEGREES, about_point=circle.get_center()))
        self.wait(2)
        
        radius_value.clear_updaters()
        diameter_value.clear_updaters()
        circumference_value.clear_updaters()

        self.play(Transform(circle, circumference))
        self.play(Create(diameter2), Create(diameter3))
        self.play(diameter1.animate.align_to(circumference,UP))
        self.play(diameter2.animate.next_to(diameter1,DOWN, buff = 0))
        self.play(diameter3.animate.next_to(diameter2,DOWN,buff = 0))
        
        tre = VGroup(diameter2,diameter3)
        bracket = BraceBetweenPoints(point_1 = diameter1.get_top(), point_2 =diameter3.get_bottom(),sharpness = 1)
        bracket_value = MathTex("3").next_to(bracket,LEFT, buff = 0.2)
        final_line = Line(color=  YELLOW).rotate(90*DEGREES).set_length((PI - 3)*2).next_to(diameter3,DOWN,buff = 0)
        bracket2 = BraceBetweenPoints(point_1 = final_line.get_top(), point_2 =final_line.get_bottom(),sharpness = 1)
        final_line_value = MathTex("0.14159...").next_to(bracket2,LEFT,buff = 0.2).set_color(WHITE)

        pi = MathTex("\\pi =" "C","/","d" ,"= 3.14159...", substrings_to_isolate = ["C","d"]).scale(1.2).next_to(circumference_value,DOWN,buff= 2).set_color_by_tex("C", TEAL_D).set_color_by_tex("d",MAROON_C)
        
        self.play(Write(bracket), Write(bracket_value))
        self.play(Create(final_line), Write(bracket2), Write(final_line_value))
        self.play(Write(pi))
        self.wait()
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait()

class i1(Scene):
    def construct(self):

        x = ValueTracker(0)
        y = ValueTracker(0)

        inizio = Tex("3.i").scale(3)
        cubic1 = MathTex('x = \\sqrt[3]{\\left(\\frac{b^3}{27a^3}+\\frac{bc}{6a^2} -\\frac{d}{2a}\\right) +\\sqrt{\\left(\\frac{-b^3}{27a^3}+\\frac{bc}{6a^2} -\\frac{d}{2a}\\right)^2+\\left(\\frac{c}{3a} -\\frac{b^2}{9a^2}\\right)^3}} ').scale(0.5).to_edge(LEFT,buff = 0.3)
        cubic2 = MathTex("+ \\sqrt[3]{\\left(\\frac{-b^3}{27a^3}+\\frac{bc}{6a^2} -\\frac{d}{2a}\\right) -\\sqrt{\\left(\\frac{-b^3}{27a^3}+\\frac{bc}{6a^2} -\\frac{d}{2a}\\right)^2+\\left(\\frac{c}{3a} -\\frac{b^2}{9a^2}\\right)^3}} -\\frac{b}{3a}").scale(0.5).next_to(cubic1,DOWN,buff = 0.2)
        gerolamo = ImageMobject("gerolamo").to_edge(RIGHT,buff =2).scale(2)
        gerolamo_scritta = Tex("Gerolamo Cardano").scale(1.5).shift(LEFT*3)
        
        cubic = VGroup(cubic1,cubic2)
        
        self.play(Write(inizio))
        self.wait()
        self.play(Unwrite(inizio))

        self.play(FadeIn(gerolamo),Write(gerolamo_scritta))
        self.play(gerolamo_scritta.animate.shift(UP*3))
        self.wait()
        self.play(Write(cubic), run_time = 5)
        self.play(FadeOut(gerolamo), Unwrite(gerolamo_scritta), Unwrite(cubic))

        s_text = Tex("Erwin Schrödinger").to_edge(UP,buff = 1).scale(1.5).shift(RIGHT*3)
        shrodinger= ImageMobject("shrodinger").to_edge(LEFT, buff = 1).scale(1.5)
        shr_equation = MathTex(r"i \hbar \frac{\partial}{\partial t}\Psi(\mathbf{r},t) = \hat H \Psi(\mathbf{r},t)").shift(RIGHT*3)

        self.play(FadeIn(shrodinger), Write(s_text))
        self.play(Write(shr_equation))
        self.wait()
        self.play(Unwrite(shr_equation),  Unwrite(s_text))
        self.play(FadeOut(shrodinger))
        self.wait()
        
        axes = ComplexPlane(color = WHITE)
        moving_axes = axes.copy().set_color(BLUE_E)
        moving_axes.prepare_for_nonlinear_transform()
        moving_axes1 = axes.copy().set_color(BLUE_E)
        moving_axes1.prepare_for_nonlinear_transform()
        
        axes.set_opacity(0.3)
        axes.add_coordinates(font_size =24)

        funz1 = MathTex("f(z) = z^2").to_edge(UL,buff = 1)
        funz2 = MathTex("f(z) = e^z").to_edge(UL,buff =1 )
    

        dot = always_redraw(lambda : Dot(color = YELLOW_B).move_to(axes.c2p(x.get_value(),y.get_value())))
        cos_line = always_redraw(lambda : Line(color = TEAL_D,start = ORIGIN, end = axes.c2p(dot.get_x(),0)))
        sin_line = always_redraw(lambda : Line(color = MAROON_C,start = ORIGIN, end = axes.c2p(0,dot.get_y())))

        dashed_cos = always_redraw(lambda : DashedLine(color = MAROON_A, start = axes.c2p(0,dot.get_y()), end = axes.c2p(dot.get_x(),dot.get_y())))
        dashed_sin = always_redraw(lambda : DashedLine(color = TEAL_A, start = axes.c2p(dot.get_x(),0), end = axes.c2p(dot.get_x(),dot.get_y())))   
        mod = always_redraw(lambda: Line(start = ORIGIN, end = dot.get_center()).set_color(GREEN_A))
        a = MathTex("a").set_color(TEAL_D).add_updater(lambda x : x.next_to(cos_line,DOWN,buff = 0.2))
        b = MathTex("b").set_color(MAROON_C).add_updater(lambda x:x.next_to(sin_line,LEFT,buff = 0.2))
        
        label1 = MathTex("3 +3i").next_to(axes.c2p(3,3), UR *0.3, buff = 0.5)
        label2 = MathTex("-2 + 1i").next_to(axes.c2p(-2,1), UL *0.3,buff = 0.5)
        label3 = MathTex("1 - 3i").next_to(axes.c2p(1,-3), DR *0.3,buff = 0.5)

        scritta = MathTex("z" ,"=", "a", "+", "b","i").to_edge(UL,buff = 1)
        scritta[2].set_color(TEAL_D)
        scritta[4].set_color(MAROON_C)
        scritta[0].set_color(YELLOW_B)
        modulus = MathTex("\\left|z\\right|","=","\\sqrt{a^2+b^2}", substrings_to_isolate =["a","b"]).next_to(scritta,DOWN,buff = 0.2)
        modulus[0].set_color(GREEN_A)
        modulus.set_color_by_tex("a", TEAL_D)
        modulus.set_color_by_tex("b",MAROON_C)

        self.play(Write(axes),FadeIn(moving_axes), FadeIn(moving_axes1))
        self.wait()
        self.play(Write(funz1),moving_axes.animate.apply_complex_function(lambda z : z**2), run_time = 2)
        self.wait()
        self.add(moving_axes1)
        self.play(FadeOut(moving_axes),Unwrite(funz1))
        self.wait()
        self.play(Write(funz2),moving_axes1.animate.apply_complex_function(np.exp), run_time = 2)
        self.wait()
        self.play(FadeOut(moving_axes1),Unwrite(funz2))
        self.play(Create(dot))
        self.wait()
        self.play(Write(cos_line),Write(sin_line), Write(dashed_cos), Write(dashed_sin), Write(scritta), Write(modulus),Write(mod))
        self.play(x.animate.set_value(1), y.animate.set_value(1))
        self.play(Write(a), Write(b))
        self.play(x.animate.set_value(3), y.animate.set_value(3))
        self.play(Write(label1))
        self.wait()
        self.play(Unwrite(label1))
        self.wait()
        self.play(x.animate.set_value(-2), y.animate.set_value(1))
        self.play(Write(label2))
        self.wait()
        self.play(Unwrite(label2))
        self.wait()
        self.play(x.animate.set_value(1), y.animate.set_value(-3))
        self.play(Write(label3))
        self.wait()
        self.play(Unwrite(label3))
        self.wait()
        self.play(x.animate.set_value(2), y.animate.set_value(2))
        self.wait(2)
        self.play(Unwrite(a), Unwrite(b),Unwrite(axes),Uncreate(dashed_cos), Uncreate(dashed_sin), Uncreate(cos_line), Uncreate(sin_line), Uncreate(dot), Unwrite(scritta), Unwrite(modulus), Uncreate(mod))
        self.wait()
        
class i2 (Scene):
    def construct(self):

        axes = ComplexPlane(x_range = [-2,2,1], y_range = [-2,2,1], x_length = 8, y_length = 8, color = BLUE_A, ).add_coordinates().to_edge(LEFT).shift(LEFT * 0.5).set_opacity(0.3)
        
        r = Line(start = axes.c2p(0,0), end = axes.c2p(1,0))
        unit_circle = Circle(color = BLUE_A, radius = r.get_length()).move_to(axes.c2p(0,0))
                
        dot = Dot(color = YELLOW_A).move_to(axes.c2p(math.sqrt(2)/2,math.sqrt(2)/2))
        cos_line = Line(color = TEAL_D,start = axes.c2p(0,0), end = axes.c2p(math.sqrt(2)/2,0))
        sin_line = Line(color = MAROON_C,start = axes.c2p(0,0), end = axes.c2p(0,math.sqrt(2)/2))

        dashed_sin = DashedLine(color = TEAL_A, start = axes.c2p(0,math.sqrt(2)/2), end = axes.c2p(math.sqrt(2)/2,math.sqrt(2)/2))
        dashed_cos = DashedLine(color = MAROON_A, start = axes.c2p(math.sqrt(2)/2,0), end = axes.c2p(math.sqrt(2)/2,math.sqrt(2)/2))

        l1 = Line(start = axes.c2p(0,0), end = axes.c2p(2,0))
        l2 = Line(start = axes.c2p(0,0), end = axes.c2p(math.sqrt(2)/2,math.sqrt(2)/2)).set_color(GREEN_A)
        z = MathTex("z = a + bi", substrings_to_isolate = ["z","a","b"]).next_to(dot,UR, buff = 0.2)
        z.set_color_by_tex("a",TEAL_D)
        z.set_color_by_tex("b",MAROON_C)
        z.set_color_by_tex("z",YELLOW_A)
        mod_z = MathTex("\\left| z \\right|","=","\\sqrt{a^{2}+b^{2}}","=1", substrings_to_isolate = ["a","b"]).to_edge(UR, buff =1.2)
        mod_z[0].set_color(GREEN_A)
        mod_z.set_color_by_tex("a", TEAL_D)
        mod_z.set_color_by_tex("b", MAROON_C)
        mod_z_label = MathTex("\\left| z \\right|").move_to(axes.c2p(0.25,0.45)).rotate(PI/4).set_color(GREEN).scale(0.7)
        cos_label = MathTex("\\cos(\\theta)").set_color(TEAL_D).scale(0.6).add_updater(lambda x : x.next_to(cos_line,DOWN,buff = 0.2))
        sin_label = MathTex("i\\sin(\\theta)").scale(0.6).set_color(MAROON_C).rotate(90*DEGREES).add_updater(lambda x:x.next_to(sin_line,LEFT,buff = 0.2))
        

        angle = Angle(l1,l2).set_color(GREEN_E)
        theta = MathTex("\\theta").move_to(axes.c2p(0.5,0.2)).set_color(GREEN_E).scale(0.8)
        
        a = MathTex("a").set_color(TEAL_D).add_updater(lambda x : x.next_to(cos_line,DOWN,buff = 0.2))
        b = MathTex("b").set_color(MAROON_C).add_updater(lambda x:x.next_to(sin_line,LEFT,buff = 0.2))
        

        self.play(Create(axes))
        self.play(Create(dot))
        self.play(Create(dashed_cos), Create(dashed_sin), Write(z), Write(a), Write(b),Create(cos_line), Create(sin_line))
        self.wait()
        self.play(Create(unit_circle))
        self.wait()
        self.play(Write(mod_z),Create(l2), Write(mod_z_label))
        self.play(Create(angle), Write(theta),z.animate.next_to(mod_z,DOWN,buff = 0.2))
        self.wait()
        a_updated = MathTex("a = \\cos(\\theta)").next_to(z, DOWN, buff = 0.2).set_color(TEAL_D)
        b_updated = MathTex("b = \\sin(\\theta)").next_to(a_updated,DOWN,buff = 0.2).set_color(MAROON_C)
        self.play(Write(a_updated), Write(b_updated))
        self.wait()
        self.play(ReplacementTransform(a,cos_label),ReplacementTransform(b,sin_label))
        self.wait()
        self.play(Unwrite(cos_label), Unwrite(sin_label), Uncreate(unit_circle), Uncreate(angle), Unwrite(theta), Unwrite(mod_z), Unwrite(z), 
                  Uncreate(l2), Unwrite(dashed_cos), Unwrite(dashed_sin), Unwrite(cos_line), Unwrite(sin_line), Uncreate(dot), Unwrite(a_updated), Unwrite(b_updated), Unwrite(axes), Unwrite(mod_z_label)) 
        self.wait()

class introduzione(Scene):
    def construct(self):

        tex1 = MathTex("Taylor \\: series").scale(1.5).to_edge(UP,buff = 0.2)
        axes = NumberPlane().set_opacity(0.3)
        
        sin = axes.plot(lambda x : np.sin(x), color = MAROON_C)
        sin_text = MathTex("y = \\sin(x)").next_to(tex1,DOWN,buff= 0.2).scale(0.8)
        
        p_text1= MathTex("f(x) = x", substrings_to_isolate= "x")
        p_text2= MathTex(r"f(x) = x - \frac{1}{3!} x^3", substrings_to_isolate= "x")
        p_text3= MathTex(r"f(x) = x- \frac{1}{3!} x^3 + \frac{1}{5!} x^5", substrings_to_isolate= "x")
        p_text4= MathTex(r"f(x) = x -\frac{1}{3!} x^3 + \frac{1}{5!} x^5 - \frac{1}{7!} x^7", substrings_to_isolate= "x")
        p_text5= MathTex(r"f(x) = x-\frac{1}{3!} x^3 + \frac{1}{5!} x^5 - \frac{1}{7!} x^7 +\frac{1}{9!} x^9 \cdots", substrings_to_isolate= "x")
        p_final_sin = MathTex(r"\sin(x)= x-\frac{1}{3!} x^3 + \frac{1}{5!} x^5 - \frac{1}{7!} x^7 +\frac{1}{9!} x^9 \cdots", substrings_to_isolate= "x").next_to(tex1,DOWN,buff=1)
        p_final_cos = MathTex(r"\cos(x) = 1-\frac{1}{2!} x^2+\frac{1}{4!} x^4-\frac{1}{6!}x^6+\frac{1}{8!}x^8 \cdots", substrings_to_isolate= "x").next_to(p_final_sin,DOWN,buff = 0.5)
        p_final_e = MathTex(r"e^x = x+ x^1 + \frac{1}{2!} x^2 + \frac{1}{3!} x^3 +\frac{1}{4!}x^4 + \frac{1}{5!}x^5  \cdots", substrings_to_isolate= "x").next_to(p_final_cos,DOWN,buff= 0.5)   
        p_text =VGroup(p_text1,p_text2,p_text3,p_text4,p_text5).next_to(sin_text,DOWN,buff = 0.2).scale(0.8)
        
        p_text1.set_color_by_tex("x",TEAL_D)
        p_text2.set_color_by_tex("x",TEAL_D)
        p_text3.set_color_by_tex("x",TEAL_D)
        p_text4.set_color_by_tex("x",TEAL_D)
        p_text5.set_color_by_tex("x",TEAL_D)
        p_final_cos.set_color_by_tex("x",TEAL_D)
        p_final_sin.set_color_by_tex("x",TEAL_D)
        p_final_e.set_color_by_tex("x",TEAL_D)
        

        p1 = axes.plot(lambda x : x )
        p2 = axes.plot(lambda x : x -x**3/math.factorial(3))
        p3 = axes.plot(lambda x : x -x**3/math.factorial(3) +x**5/math.factorial(5))
        p4 = axes.plot(lambda x : x -x**3/math.factorial(3) +x**5/math.factorial(5)-x**7/math.factorial(7))
        p5 = axes.plot(lambda x : x -x**3/math.factorial(3) +x**5/math.factorial(5)-x**7/math.factorial(7)+x**9/math.factorial(9))

        p = VGroup(p1,p2,p3,p4,p5).set_color(TEAL_D)

        self.play(Write(axes), Create(sin), Write(tex1), Create(p1))
        self.play(Write(p_text1), Write(sin_text))
        self.play(ReplacementTransform(p1,p2),ReplacementTransform(p_text1,p_text2))
        self.play(ReplacementTransform(p2,p3),ReplacementTransform(p_text2,p_text3))
        self.play(ReplacementTransform(p3,p4),ReplacementTransform(p_text3,p_text4))
        self.play(ReplacementTransform(p4,p5),ReplacementTransform(p_text4,p_text5))
        self.play(Uncreate(p5),Uncreate(sin),Unwrite(axes), Unwrite(sin_text),ReplacementTransform(p_text5,p_final_sin)) 
        self.wait()
        self.play(Write(p_final_cos), Write(p_final_e))
        self.play(Unwrite(tex1), Unwrite(p_final_sin), Unwrite(p_final_cos), Unwrite(p_final_e))
        self.wait()

class grafico3d(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range= [ -6,6,1],
            y_range= [ -6,6,1],
            z_range= [ -6,6,1],
            x_length=8,
            y_length=6,
            z_length=6,
        )
        axis_labels = axes.get_axis_labels()

        graph = ParametricFunction(lambda t : np.array([t * 0.5 , np.cos(t)  ,np.sin(t) ]),t_range = [-6, 6],color = GREEN)
        
        self.add(axes, axis_labels)
        self.wait()
        self.play(Create(graph))
        self.wait()
        self.move_camera(phi = 70 * DEGREES,  theta = -40*DEGREES)
        
class Gauss(Scene):
    def construct(self):
        plane = NumberPlane(y_range = [-3,3,1], x_range = [-3,3,1], background_line_style={"stroke_opacity": 0.2}).add_coordinates().shift(LEFT*2)
        graph = plane.plot(lambda x : math.exp(-(x)**2), color = RED_E)
        area = plane.get_area(graph, x_range=[-3,3], color = RED_A)
        scritta = MathTex(r"f(x) = \int _{-\infty}^{+\infty}e^{-x^2} = \sqrt{\pi}").next_to(graph, RIGHT, buff = 0.5).shift(UP*1).scale(0.8)
        gauss = ImageMobject("Gauss").scale(0.4).to_edge(RIGHT,buff= 0.5).shift(DOWN*2)
        
        self.add(plane, gauss)
        self.wait()
        self.play(Create(graph))
        self.wait()
        self.play(FadeIn(area), Create(scritta))
        self.wait(2)

