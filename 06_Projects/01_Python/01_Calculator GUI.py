{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "from kivy.app import App\n",
    "from kivy.uix.button import Button\n",
    "from kivy.uix.boxlayout import BoxLayout\n",
    "from kivy.uix.gridlayout import GridLayout\n",
    "from kivy.uix.label import Label"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "OSError",
     "evalue": "source code not available",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOSError\u001b[0m                                   Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [9], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[39mclass\u001b[39;00m \u001b[39mmyApp\u001b[39;00m(App):\n\u001b[0;32m      2\u001b[0m     \u001b[39mdef\u001b[39;00m \u001b[39mbuild\u001b[39m(\u001b[39mself\u001b[39m):\n\u001b[0;32m      3\u001b[0m         root_widget \u001b[39m=\u001b[39m BoxLayout(orientation\u001b[39m=\u001b[39m\u001b[39m'\u001b[39m\u001b[39mvertical\u001b[39m\u001b[39m'\u001b[39m)\n",
      "Cell \u001b[1;32mIn [9], line 37\u001b[0m, in \u001b[0;36mmyApp\u001b[1;34m()\u001b[0m\n\u001b[0;32m     35\u001b[0m     root_widget\u001b[39m.\u001b[39madd_widget(clear_button)\n\u001b[0;32m     36\u001b[0m     \u001b[39mreturn\u001b[39;00m root_widget\n\u001b[1;32m---> 37\u001b[0m myApp()\u001b[39m.\u001b[39;49mrun()\n",
      "File \u001b[1;32mc:\\Users\\soghatur\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\kivy\\app.py:954\u001b[0m, in \u001b[0;36mApp.run\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    951\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mrun\u001b[39m(\u001b[39mself\u001b[39m):\n\u001b[0;32m    952\u001b[0m     \u001b[39m'''Launches the app in standalone mode.\u001b[39;00m\n\u001b[0;32m    953\u001b[0m \u001b[39m    '''\u001b[39;00m\n\u001b[1;32m--> 954\u001b[0m     \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m_run_prepare()\n\u001b[0;32m    955\u001b[0m     runTouchApp()\n\u001b[0;32m    956\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mstop()\n",
      "File \u001b[1;32mc:\\Users\\soghatur\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\kivy\\app.py:923\u001b[0m, in \u001b[0;36mApp._run_prepare\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    921\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39mnot\u001b[39;00m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mbuilt:\n\u001b[0;32m    922\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mload_config()\n\u001b[1;32m--> 923\u001b[0m     \u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49mload_kv(filename\u001b[39m=\u001b[39;49m\u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49mkv_file)\n\u001b[0;32m    924\u001b[0m     root \u001b[39m=\u001b[39m \u001b[39mself\u001b[39m\u001b[39m.\u001b[39mbuild()\n\u001b[0;32m    925\u001b[0m     \u001b[39mif\u001b[39;00m root:\n",
      "File \u001b[1;32mc:\\Users\\soghatur\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\kivy\\app.py:676\u001b[0m, in \u001b[0;36mApp.load_kv\u001b[1;34m(self, filename)\u001b[0m\n\u001b[0;32m    674\u001b[0m \u001b[39melse\u001b[39;00m:\n\u001b[0;32m    675\u001b[0m     \u001b[39mtry\u001b[39;00m:\n\u001b[1;32m--> 676\u001b[0m         default_kv_directory \u001b[39m=\u001b[39m dirname(getfile(\u001b[39mself\u001b[39;49m\u001b[39m.\u001b[39;49m\u001b[39m__class__\u001b[39;49m))\n\u001b[0;32m    677\u001b[0m         \u001b[39mif\u001b[39;00m default_kv_directory \u001b[39m==\u001b[39m \u001b[39m'\u001b[39m\u001b[39m'\u001b[39m:\n\u001b[0;32m    678\u001b[0m             default_kv_directory \u001b[39m=\u001b[39m \u001b[39m'\u001b[39m\u001b[39m.\u001b[39m\u001b[39m'\u001b[39m\n",
      "File \u001b[1;32mc:\\Users\\soghatur\\AppData\\Local\\Programs\\Python\\Python310\\lib\\inspect.py:785\u001b[0m, in \u001b[0;36mgetfile\u001b[1;34m(object)\u001b[0m\n\u001b[0;32m    783\u001b[0m             \u001b[39mreturn\u001b[39;00m module\u001b[39m.\u001b[39m\u001b[39m__file__\u001b[39m\n\u001b[0;32m    784\u001b[0m         \u001b[39mif\u001b[39;00m \u001b[39mobject\u001b[39m\u001b[39m.\u001b[39m\u001b[39m__module__\u001b[39m \u001b[39m==\u001b[39m \u001b[39m'\u001b[39m\u001b[39m__main__\u001b[39m\u001b[39m'\u001b[39m:\n\u001b[1;32m--> 785\u001b[0m             \u001b[39mraise\u001b[39;00m \u001b[39mOSError\u001b[39;00m(\u001b[39m'\u001b[39m\u001b[39msource code not available\u001b[39m\u001b[39m'\u001b[39m)\n\u001b[0;32m    786\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mTypeError\u001b[39;00m(\u001b[39m'\u001b[39m\u001b[39m{!r}\u001b[39;00m\u001b[39m is a built-in class\u001b[39m\u001b[39m'\u001b[39m\u001b[39m.\u001b[39mformat(\u001b[39mobject\u001b[39m))\n\u001b[0;32m    787\u001b[0m \u001b[39mif\u001b[39;00m ismethod(\u001b[39mobject\u001b[39m):\n",
      "\u001b[1;31mOSError\u001b[0m: source code not available"
     ]
    }
   ],
   "source": [
    "class myApp(App):\n",
    "    def build(self):\n",
    "        root_widget = BoxLayout(orientation='vertical')\n",
    "        output_label = Label(size_hint_y = 0.75, font_size=50)\n",
    "        button_symbols = ('1', '2', '3', '+',\n",
    "                          '4', '5', '6', '-',\n",
    "                          '7', '8', '9', '.',\n",
    "                          '0', '*', '/', '=')\n",
    "        button_grid = GridLayout(cols=4, size_hint_y=2)\n",
    "        for symbol in button_symbols:\n",
    "            button_grid.add_widget(Button(text=symbol))\n",
    "\n",
    "        clear_button = Button(text = 'Clear', size_hint_y=None, height=100)\n",
    "        def print_button_text(instance):\n",
    "            output_label.text += instance.text\n",
    "        for button in button_grid.children[1:]:\n",
    "            button.bind(on_press=print_button_text)\n",
    "        def resize_label_text(label, new_height):\n",
    "            label.fontsize = 0.5*label.height\n",
    "        output_label.bind(height=resize_label_text)\n",
    "\n",
    "        def evaluate_result(instance):\n",
    "            try:\n",
    "                output_label.text = str(eval(output_label.text))\n",
    "            except SyntaxError:\n",
    "                output_label.text = 'Python Syntax error!'\n",
    "        button_grid.children[0].bind(on_press=evaluate_result)\n",
    "\n",
    "        def clear_label(instance):\n",
    "            output_label.text = \" \"\n",
    "        clear_button.bind(on_press=clear_label)\n",
    "\n",
    "        root_widget.add_widget(output_label)\n",
    "        root_widget.add_widget(button_grid)\n",
    "        root_widget.add_widget(clear_button)\n",
    "        return root_widget\n",
    "    myApp().run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.8 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "cddf2645a6a3ab2d03dc52c73588f8603eb596e75ff57e7d6cdffdd4fb718815"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
